"""EGID / EGRID / Parzelle für alle Gebäude an den Geschäftsstrassen der Retail-Map-Städte.

Quelle der Adressen: amtliches Gebäude- und Wohnungsregister (GWR, ch.bfs.gebaeude_wohnungs_register)
über api3.geo.admin.ch, abgefragt pro Strasse über die Strassen-ID (ESID aus dem amtlichen
Strassenverzeichnis). Dazu ergänzt: Adressen, die nur in OSM oder nur im SEED der Retail Map stehen.
Parzelle/EGRID: GWR-Felder egrid/lparz/lgbkr, gegengeprüft mit der amtlichen Vermessung
(ch.swisstopo-vd.stand-oerebkataster, identify am Gebäudepunkt) – AV gilt bei Abweichung.

Schreibt NICHT in index.html. Liest SEED nur (seed.load()).
Aufruf:
  python3 egid_highstreets.py                     # alle 8 Städte
  python3 egid_highstreets.py --staedte Bern,Basel
  python3 egid_highstreets.py --out ~/Downloads/xyz
Cache: tools/cache/egid_av.json (Identify-Ergebnisse je EGID), Rerun ist dadurch schnell.
"""
import argparse, csv, json, math, re, sys, time, unicodedata, urllib.parse, urllib.request
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))
import seed  # noqa: E402
from topstrassen import overpass  # noqa: E402

API = "https://api3.geo.admin.ch/rest/services/api"
UA = {"User-Agent": "kuroiwa-retailmap/1.0 (egid_highstreets)"}
PAUSE = 0.25
STAND = time.strftime("%Y-%m-%d")

# ---------------------------------------------------------------- Konfiguration
# prio1 = Top-Strassen (staedte.json) + von Kaito genannte Toplagen; weitere Strassen aus CITIES (index.html) = prio 2.
STAEDTE = {
    "Zürich (Kreis 1)": dict(kt="ZH", bfs=[261], key="zürich (kreis 1)", plz=[8001], haupt="Bahnhofstrasse", radius=None,
                             prio1=["Bahnhofstrasse", "Rennweg", "Storchengasse", "Augustinergasse", "Löwenstrasse", "Limmatquai",
                                    "Niederdorfstrasse", "Strehlgasse", "In Gassen", "Poststrasse", "Paradeplatz", "Münsterhof"]),
    "Bern": dict(kt="BE", bfs=[351], key="bern", haupt="Marktgasse", radius=1300,
                 prio1=["Spitalgasse", "Marktgasse", "Kramgasse", "Gerechtigkeitsgasse", "Münstergasse"]),
    "Basel": dict(kt="BS", bfs=[2701], key="basel", haupt="Freie Strasse", radius=1500,
                  prio1=["Freie Strasse", "Gerbergasse", "Steinenvorstadt", "Marktplatz", "Eisengasse"]),
    "Genf": dict(kt="GE", bfs=[6621], key="genf", haupt="Rue du Rhône", radius=1300,
                 prio1=["Rue du Rhône", "Rue de la Confédération", "Rue du Marché", "Rue de la Croix-d'Or", "Rue de Rive",
                        "Rue du Mont-Blanc"]),
    "Lausanne": dict(kt="VD", bfs=[5586], key="lausanne", haupt="Rue de Bourg", radius=1000,
                     prio1=["Rue de Bourg", "Rue Saint-François", "Place Saint-François", "Rue du Pont", "Rue Centrale",
                            "Rue Haldimand"]),
    "St. Gallen": dict(kt="SG", bfs=[3203], key="st. gallen", haupt="Multergasse", radius=1000,
                       prio1=["Multergasse", "Marktgasse", "Spisergasse", "Neugasse", "Webergasse"]),
    "St. Moritz": dict(kt="GR", bfs=[3787], key="st. moritz", haupt="Via Maistra", radius=1200,
                       prio1=["Via Serlas", "Via Maistra", "Via dal Bagn", "Plazza dal Mulin", "Via dal Vout"]),
    "Gstaad": dict(kt="BE", bfs=[843], key="gstaad", haupt="Promenade", radius=900,
                   prio1=["Promenade", "Lauenenstrasse", "Palacestrasse", "Untergstaadstrasse", "Güterstrasse"]),
}
# Abweichende Schreibweisen (Retail Map/OSM → amtliches Strassenverzeichnis), nur falls exakte Suche leer bleibt
ALIAS = {"Place St-François": "Place Saint-François", "Petit-Chêne": "Rue du Petit-Chêne", "Rue Haldimand": "Rue William-Haldimand"}

GKAT = {1010: "Provisorische Unterkunft", 1020: "Reines Wohngebäude", 1030: "Wohngebäude mit Nebennutzung",
        1040: "Gebäude mit teilweiser Wohnnutzung", 1060: "Gebäude ohne Wohnnutzung", 1080: "Sonderbau"}
GKLAS = {1110: "Einfamilienhaus", 1121: "Zweifamilienhaus", 1122: "Mehrfamilienhaus", 1130: "Wohngebäude für Gemeinschaften",
         1211: "Hotel", 1212: "Andere kurzfristige Beherbergung", 1220: "Bürogebäude", 1230: "Gross- und Einzelhandel",
         1231: "Restaurant/Bar", 1241: "Verkehr/Nachrichtenwesen", 1242: "Garagengebäude", 1251: "Industriegebäude",
         1252: "Behälter/Silo/Lager", 1261: "Kultur/Freizeit", 1262: "Museum/Bibliothek", 1263: "Schule/Hochschule/Forschung",
         1264: "Spital/Heim", 1265: "Sporthalle", 1271: "Landwirtschaft", 1272: "Kirche/Kultus", 1273: "Denkmal",
         1274: "Sonstiger Hochbau", 1275: "Kollektivunterkunft", 1276: "Tierhaltung", 1277: "Pflanzenbau", 1278: "Andere Landwirtschaft"}
GBAUP = {8011: "vor 1919", 8012: "1919–1945", 8013: "1946–1960", 8014: "1961–1970", 8015: "1971–1980", 8016: "1981–1985",
         8017: "1986–1990", 8018: "1991–1995", 8019: "1996–2000", 8020: "2001–2005", 8021: "2006–2010", 8022: "2011–2015",
         8023: "ab 2016"}
GSTAT = {1001: "projektiert", 1002: "bewilligt", 1003: "im Bau", 1004: "bestehend", 1005: "nicht nutzbar",
         1007: "abgebrochen", 1008: "nicht realisiert"}

COLS = ["Prio", "Stadt", "Strasse", "Hausnummer", "Retail-Map-Key", "In OSM", "Adressquelle", "EGID", "EGRID", "Parzelle",
        "Grundstücksart", "Grundbuchkreis", "Gemeinde", "BFS-Nr", "Kanton", "PLZ", "E (LV95)", "N (LV95)", "Lat", "Lon",
        "Gebäudekategorie", "Gebäudeklasse", "Baujahr/Periode", "Geschosse", "Wohnungen", "Grundfläche m²", "Gebäudestatus",
        "Weitere Rechte am Punkt", "Abfrage", "Mieter (OSM)", "Eigentümer bekannt (Retail Map)", "Eigentümer-Register 05.11.",
        "Hinweis", "Link Eigentümerauskunft", "Link ÖREB-Auszug", "Link Karte", "Eigentümer", "Datum Auskunft", "Quelle"]


# ---------------------------------------------------------------- HTTP
def get(url, tries=4):
    err = None
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                d = json.load(r)
            time.sleep(PAUSE)
            return d
        except Exception as e:
            err = e
            time.sleep(3 * (i + 1))
    raise err


def find(layer, field, text, contains=False):
    q = urllib.parse.urlencode({"layer": layer, "searchField": field, "searchText": text,
                                "contains": str(contains).lower(), "returnGeometry": "false"})
    return get(f"{API}/MapServer/find?{q}").get("results", [])


# ---------------------------------------------------------------- Helfer
def norm(s):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    s = s.replace("saint-", "st-").replace("sankt ", "st. ")
    return re.sub(r"[^a-z0-9]", "", s)


def hn_key(h):
    return re.sub(r"\s+", "", str(h)).lower()


def hn_sort(h):
    m = re.match(r"(\d+)(.*)", str(h))
    return (int(m.group(1)), m.group(2)) if m else (99999, str(h))


def lv95_wgs(e, n):
    y, x = (e - 2600000) / 1e6, (n - 1200000) / 1e6
    lam = 2.6779094 + 4.728982 * y + 0.791484 * y * x + 0.1306 * y * x * x - 0.0436 * y ** 3
    phi = 16.9023892 + 3.238272 * x - 0.270978 * y * y - 0.002528 * x * x - 0.0447 * y * y * x - 0.0140 * x ** 3
    return round(phi * 100 / 36, 6), round(lam * 100 / 36, 6)


def cities_streets():
    """Kuratierte Strassenlisten aus CITIES in index.html (nur lesen)."""
    html = (TOOLS.parent / "index.html").read_text()
    return {m.group(1): [s.replace("\\'", "'") for s in re.findall(r"'((?:[^'\\]|\\.)*)'", m.group(2))]
            for m in re.finditer(r"^ '([^']+)': \{q:'[^']*', streets:\[(.*?)\]\}", html, re.M)}


def esids(strasse, bfs):
    """Strassen-IDs im amtlichen Strassenverzeichnis (exakter Name, sonst Alias/normalisierter Vergleich)."""
    for name in [strasse, ALIAS.get(strasse)]:
        if not name:
            continue
        hits = [r["attributes"] for r in find("ch.swisstopo.amtliches-strassenverzeichnis", "stn_label", name)
                if r["attributes"].get("com_fosnr") in bfs]
        ex = [a for a in hits if norm(a["stn_label"]) == norm(name)]
        if ex:
            return [(a["str_esid"], a["stn_label"]) for a in ex]
        # find ist case-sensitiv (z.B. «Quai du Général-GUISAN»): Teilwortsuche, dann normalisiert vergleichen
        wort = max(re.split(r"[\s\-']", name), key=len)
        for w in {wort, wort.upper(), wort.capitalize()}:
            hits = [r["attributes"] for r in find("ch.swisstopo.amtliches-strassenverzeichnis", "stn_label", w, True)
                    if r["attributes"].get("com_fosnr") in bfs and norm(r["attributes"]["stn_label"]) == norm(name)]
            if hits:
                return [(a["str_esid"], a["stn_label"]) for a in hits]
    return []


def gwr_by_esid(esid):
    return [r["attributes"] for r in find("ch.bfs.gebaeude_wohnungs_register", "esid", str(esid))]


def gwr_by_egid(egid):
    return [r["attributes"] for r in find("ch.bfs.gebaeude_wohnungs_register", "egid", str(egid))]


def search_address(strasse, hn, gemeinde_bfs):
    """Fallback: SearchServer, Hausnummer mit Wortgrenze geprüft."""
    q = urllib.parse.quote(f"{strasse} {hn}")
    res = get(f"{API}/SearchServer?type=locations&origins=address&sr=2056&limit=20&searchText={q}").get("results", [])
    pat = re.compile(r"^" + re.escape(norm(strasse)) + re.escape(hn_key(hn)) + r"$")
    for r in res:
        a = r["attrs"]
        det = a.get("detail", "")
        if not any(f" {b} " in f" {det} " for b in gemeinde_bfs):
            continue
        lab = re.sub("<[^>]+>", "", a["label"]).split("  ")[0]
        lab_addr = re.sub(r"\s\d{4}\s.*$", "", lab)
        if pat.match(norm(lab_addr)):
            return str(a.get("featureId", "")).split("_")[0] or None
    return None


# ---------------------------------------------------------------- Amtliche Vermessung (mit Cache)
CACHE_F = TOOLS / "cache" / "egid_av.json"


def load_cache():
    try:
        return json.loads(CACHE_F.read_text())
    except Exception:
        return {}


def av_identify(e, n):
    q = urllib.parse.urlencode({"geometryType": "esriGeometryPoint", "geometry": f"{e},{n}", "sr": "2056",
                                "layers": "all:ch.swisstopo-vd.stand-oerebkataster", "tolerance": "0",
                                "returnGeometry": "false"})
    out = []
    for r in get(f"{API}/MapServer/identify?{q}").get("results", []):
        a = r["attributes"]
        if not a.get("egris_egrid"):
            continue
        out.append({"nr": a.get("number"), "egrid": a.get("egris_egrid"), "typ": a.get("realestate_type") or "",
                    "pdf": a.get("oereb_extract_pdf") or "", "bfs": a.get("bfs_nr")})
    return out


# ---------------------------------------------------------------- Links / Portale
def portal_link(kt, egrid, lgbkr, parz, e, n):
    if kt == "ZH" and egrid:
        return f"https://portal.objektwesen.zh.ch/aks/detail?egrid={egrid}&bfsNr=261"
    if kt == "GE" and parz and lgbkr:
        return f"https://ge.ch/terextraitfoncier/rapport.aspx?commune={lgbkr}&parcelle={parz}"
    if kt == "BS" and e:
        return f"https://map.geo.bs.ch/theme/Amtliche%20Vermessung?map_x={int(e)}&map_y={int(n)}&map_zoom=12&map_crosshair=true"
    if kt == "BE":
        return "https://www.grudis-public.apps.be.ch (AGOV-Login, Suche über E-GRID)"
    if kt == "VD":
        return "https://intercapi-public.vd.ch/territoire/intercapi-public/ (SMS, 5/Tag)"
    if kt == "GR":
        return "https://map.geo.gr.ch/public/theme/uGSP_Grundstueckabfrage (Captcha)"
    if kt == "SG":
        return "keine Online-Auskunft: schriftlich ans Grundbuchamt Stadt St. Gallen (siehe Anleitung)"
    return ""


def map_link(e, n):
    return (f"https://map.geo.admin.ch/?E={e}&N={n}&zoom=13&crosshair=marker&layers=ch.kantone.cadastralwebmap-farbe"
            if e else "")


def parz_label(kt, gemeinde, lgbkr, parz):
    if not parz:
        return ""
    if kt == "BE" and lgbkr:
        return f"{gemeinde} {lgbkr} / {parz}"
    if kt == "BS" and lgbkr:
        return f"{parz} (Sektion {lgbkr})"
    if kt == "GE" and lgbkr:
        return f"{parz} (commune cadastrale {lgbkr})"
    return str(parz)


# ---------------------------------------------------------------- Bestand (SEED + Register)
def load_register():
    f = Path.home() / "Downloads/Retail Map Anfragen/Eigentuemer_Register_Treffer_2026-11-05.csv"
    reg = {}
    if not f.exists():
        return reg
    with open(f, encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh, delimiter=";"):
            k = (r.get("Key") or "").strip()
            if not k:
                continue
            art = r.get("Art", "")
            txt = r.get("Eigentümer neu") or ""
            if art in ("owner", "bestätigt") and txt:
                reg.setdefault(k, []).append(txt)
            elif txt or r.get("Quelle/Notiz"):
                reg.setdefault(k, []).append(f"[{art}] {txt or r.get('Quelle/Notiz', '')[:120]}")
    return reg


# ---------------------------------------------------------------- Kern
def osm_adressen(streets, lat, lon, radius):
    rx = "^(" + "|".join(re.escape(s) for s in streets) + ")$"
    q = (f'[out:json][timeout:180];nwr(around:{radius},{lat},{lon})["addr:street"~"{rx}"]["addr:housenumber"];'
         f"out center tags;")
    adr = {}
    for el in overpass(q)["elements"]:
        t = el["tags"]
        for h in re.split(r"[;,]", t["addr:housenumber"]):
            h = h.strip()
            if not h:
                continue
            a = adr.setdefault((norm(t["addr:street"]), hn_key(h)), {"street": t["addr:street"], "hn": h, "mieter": []})
            name = t.get("brand") or t.get("name")
            if name and any(x in t for x in ("shop", "amenity", "office", "craft", "tourism")) and name not in a["mieter"]:
                a["mieter"].append(name)
    return adr


def run_city(stadt, cfg, cstreets, sd, reg, cache, log):
    kt, bfs = cfg["kt"], cfg["bfs"]
    prio1 = cfg["prio1"]
    extra = [s for s in cstreets.get(stadt, []) if s not in prio1]
    streets = prio1 + extra
    log(f"{stadt}: {len(streets)} Strassen")
    recs, street_name, missing_streets = [], {}, []
    for s in streets:
        ids = esids(s, bfs)
        if not ids:
            missing_streets.append(s)
            log(f"  Strasse nicht im amtlichen Verzeichnis: {s}")
            continue
        for esid, label in ids:
            street_name[norm(label)] = s
            for a in gwr_by_esid(esid):
                if a.get("ggdenr") not in bfs or a.get("gstat") in (1007, 1008):
                    continue
                if cfg.get("plz") and a.get("dplz4") not in cfg["plz"]:
                    continue
                a["_strasse_cfg"] = s
                recs.append(a)
    # Zentrum = Median der Hauptstrasse
    hp = [a for a in recs if a["_strasse_cfg"] == cfg["haupt"] and a.get("dkode")]
    ce = sorted(a["dkode"] for a in hp)[len(hp) // 2]
    cn = sorted(a["dkodn"] for a in hp)[len(hp) // 2]
    clat, clon = lv95_wgs(ce, cn)
    ausserhalb = 0
    if cfg.get("radius"):
        keep = []
        for a in recs:
            e, n = a.get("dkode") or a.get("gkode"), a.get("dkodn") or a.get("gkodn")
            if e and math.hypot(e - ce, n - cn) > cfg["radius"]:
                ausserhalb += 1
                continue
            keep.append(a)
        recs = keep
    # OSM
    try:
        osm = osm_adressen(sorted(set(streets) | {a["strname"][0] for a in recs if a.get("strname")}), clat, clon,
                           (cfg.get("radius") or 1500) + 150)
    except Exception as ex:
        log(f"  Overpass fehlgeschlagen: {ex}")
        osm = None
    osm_street = {}
    for (ns, _), v in (osm or {}).items():
        osm_street.setdefault(ns, v["street"])

    rows, seen = [], set()

    def add_row(a, strasse_cfg, hn, quelle):
        amtl = (a.get("strname") or [""])[0]
        cands = [x for x in (osm_street.get(norm(amtl)), osm_street.get(norm(strasse_cfg))) if x]
        # bevorzugt die OSM-Schreibweise, unter der diese Hausnummer tatsächlich in OSM steht
        s_osm = next((x for x in cands if (norm(x), hn_key(hn)) in (osm or {})), cands[0] if cands else strasse_cfg)
        k = (norm(s_osm), hn_key(hn))
        if k in seen:
            return
        seen.add(k)
        rows.append({"a": a, "strasse": s_osm, "hn": hn, "quelle": quelle,
                     "osm": None if osm is None else (k in osm), "mieter": (osm or {}).get(k, {}).get("mieter", [])})

    for a in recs:
        add_row(a, a["_strasse_cfg"], a.get("deinr") or "", "GWR")
    # Adressen nur in OSM oder nur im SEED
    nur = []
    for (ns, h), v in (osm or {}).items():
        if (ns, h) not in seen and ns in {norm(s) for s in streets}:
            nur.append((v["street"], v["hn"], "nur OSM"))
    snorm = {norm(s) for s in streets}
    for key in sd:
        p = key.split("|")
        if len(p) == 3 and p[0] == cfg["key"] and norm(p[1]) in snorm and (norm(p[1]), hn_key(p[2])) not in seen:
            orig = next((s for s in streets if norm(s) == norm(p[1])), p[1])
            nur.append((orig, p[2], "nur Retail Map SEED"))
    for s, h, q in nur:
        if (norm(s), hn_key(h)) in seen:
            continue
        egid = None
        try:
            egid = search_address(s, h, bfs)
        except Exception:
            pass
        a = {}
        m = re.fullmatch(r"(\d+[a-z]?)\s*[-–]\s*(\d+[a-z]?)", hn_key(h))
        if m:  # OSM-Sammeladresse «9-11»: GWR führt die Einzelnummern
            g = [x for x in recs if norm(x["_strasse_cfg"]) == norm(s) and hn_key(x.get("deinr", "")) in m.groups()]
            if g:
                add_row(g[0], s, h, f"nur OSM (Sammeladresse, GWR: {' / '.join(m.groups())})")
                continue
        if egid:
            g = gwr_by_egid(egid)
            a = next((x for x in g if hn_key(x.get("deinr", "")) == hn_key(h)), g[0] if g else {})
            if a and a.get("ggdenr") not in bfs:
                a = {}
        add_row(a, s, h, q + (" (EGID via Adresssuche)" if a else " (kein GWR-Treffer)"))

    # AV-Identify je EGID
    for r in rows:
        a = r["a"]
        eg = a.get("egid")
        if not eg or eg in cache:
            continue
        e, n = a.get("gkode") or a.get("dkode"), a.get("gkodn") or a.get("dkodn")
        if not e:
            cache[eg] = []
            continue
        try:
            cache[eg] = av_identify(e, n)
        except Exception as ex:
            log(f"  identify {eg} fehlgeschlagen: {ex}")
    # Zeilen aufbauen
    p1n = {norm(s) for s in prio1} | {norm(ALIAS[s]) for s in prio1 if s in ALIAS}
    out, parz_first = [], {}
    rows.sort(key=lambda r: (streets.index(next((s for s in streets if norm(s) == norm(r["strasse"])), streets[0]))
                             if any(norm(s) == norm(r["strasse"]) for s in streets) else 99, hn_sort(r["hn"])))
    for r in rows:
        a = r["a"]
        key = f"{cfg['key']}|{r['strasse'].lower()}|{str(r['hn']).lower()}"
        av = cache.get(a.get("egid"), []) if a.get("egid") else []
        lieg = [x for x in av if x["typ"] == "Liegenschaft"] or av
        gwr_egrid, gwr_parz = a.get("egrid") or "", (a.get("lparz") or "")
        prim = next((x for x in lieg if x["egrid"] == gwr_egrid), None) or (lieg[0] if lieg else None)
        hinweis = []
        if prim and gwr_egrid and gwr_egrid not in {x["egrid"] for x in av}:
            # Gebäudepunkt liegt in der AV auf einer anderen Parzelle als die GWR-Verknüpfung → GWR gilt, Hinweis
            base = re.sub(r"EGRID=.*$", "EGRID=", prim["pdf"]) if prim["pdf"] else ""
            hinweis.append(f"Gebäudepunkt liegt in der AV auf {prim['typ']} {prim['nr']} ({prim['egrid']}); "
                           f"GWR verknüpft {gwr_egrid}/{gwr_parz} – im Plan prüfen")
            prim = {"egrid": gwr_egrid, "nr": gwr_parz, "typ": "lt. GWR", "pdf": base + gwr_egrid if base else ""}
        if prim:
            egrid, parz = prim["egrid"], prim["nr"] or gwr_parz
            typ = prim["typ"]
            if gwr_egrid and gwr_egrid != egrid:
                g = next((x for x in av if x["egrid"] == gwr_egrid), None)
                hinweis.append(f"GWR nennt EGRID {gwr_egrid}" + (f" ({g['typ']} {g['nr']})" if g else "")
                               + "; hier Liegenschaft aus amtlicher Vermessung")
        else:
            egrid, parz, typ = gwr_egrid, gwr_parz, ""
            if a.get("egid"):
                hinweis.append("Parzelle nur aus GWR (AV-Abfrage ohne Treffer)")
        weitere = "; ".join(f"{x['typ']} {x['nr']} {x['egrid']}" for x in av
                            if prim and x["egrid"] != prim["egrid"] and x["typ"] != "Liegenschaft")
        if any(x["typ"].startswith("SelbstRecht") for x in av):
            hinweis.append("Baurecht/selbständiges Recht am Gebäudepunkt: Gebäudeeigentümer kann vom Landeigentümer abweichen, "
                           "beide abfragen")
        if not a.get("egid"):
            hinweis.append("kein EGID gefunden – Adresse im amtlichen Register nicht vorhanden oder abweichend")
        if r["osm"] is False:
            hinweis.append("fehlt in OSM: Key erscheint in der Karte nur über EXTRA")
        if r["strasse"] != (a.get("strname") or [r["strasse"]])[0]:
            hinweis.append(f"amtlicher Strassenname: {(a.get('strname') or [''])[0]}")
        e, n = a.get("gkode") or a.get("dkode") or "", a.get("gkodn") or a.get("dkodn") or ""
        lat, lon = lv95_wgs(e, n) if e else ("", "")
        abfrage = "ja"
        pk = egrid or None
        if pk:
            if pk in parz_first:
                abfrage = f"gleiche Parzelle wie {parz_first[pk]}"
            else:
                parz_first[pk] = f"{r['strasse']} {r['hn']}"
        rec = sd.get(key, {})
        owner = rec.get("owner", "")
        lgbkr = a.get("lgbkr") or ""
        lgbkr = "" if lgbkr in (0, "0") else lgbkr
        bj = a.get("gbauj") or GBAUP.get(a.get("gbaup"), "")
        pdf = (prim or {}).get("pdf", "")
        out.append({
            "Prio": 1 if norm(r["strasse"]) in p1n else 2, "Stadt": stadt, "Strasse": r["strasse"], "Hausnummer": r["hn"],
            "Retail-Map-Key": key, "In OSM": {True: "ja", False: "nein", None: "?"}[r["osm"]], "Adressquelle": r["quelle"],
            "EGID": a.get("egid", ""), "EGRID": egrid, "Parzelle": parz_label(kt, a.get("ggdename", ""), lgbkr, parz),
            "Grundstücksart": typ, "Grundbuchkreis": lgbkr, "Gemeinde": a.get("ggdename", ""), "BFS-Nr": a.get("ggdenr", ""),
            "Kanton": kt, "PLZ": a.get("dplz4", ""), "E (LV95)": e, "N (LV95)": n, "Lat": lat, "Lon": lon,
            "Gebäudekategorie": GKAT.get(a.get("gkat"), a.get("gkat") or ""),
            "Gebäudeklasse": GKLAS.get(a.get("gklas"), a.get("gklas") or ""), "Baujahr/Periode": bj,
            "Geschosse": a.get("gastw") or "", "Wohnungen": a.get("ganzwhg") or "", "Grundfläche m²": a.get("garea") or "",
            "Gebäudestatus": GSTAT.get(a.get("gstat"), ""), "Weitere Rechte am Punkt": weitere, "Abfrage": abfrage,
            "Mieter (OSM)": " · ".join(r["mieter"]), "Eigentümer bekannt (Retail Map)": owner,
            "Eigentümer-Register 05.11.": " | ".join(reg.get(key, [])), "Hinweis": "; ".join(hinweis),
            "Link Eigentümerauskunft": portal_link(kt, egrid, lgbkr, parz, e, n), "Link ÖREB-Auszug": pdf,
            "Link Karte": map_link(e, n), "Eigentümer": "", "Datum Auskunft": "", "Quelle": "",
        })
    # Eigentümer auf gleiche Parzelle übertragen (nur als Hinweis)
    par_owner = {}
    for o in out:
        if o["EGRID"] and (o["Eigentümer bekannt (Retail Map)"] or o["Eigentümer-Register 05.11."]):
            par_owner.setdefault(o["EGRID"], f"{o['Strasse']} {o['Hausnummer']}")
    for o in out:
        if (o["EGRID"] in par_owner and not o["Eigentümer bekannt (Retail Map)"] and not o["Eigentümer-Register 05.11."]
                and par_owner[o["EGRID"]] != f"{o['Strasse']} {o['Hausnummer']}"):
            o["Hinweis"] = "; ".join(x for x in [o["Hinweis"], f"Eigentümer der Parzelle bekannt über {par_owner[o['EGRID']]}"] if x)
    stat = {"strassen": len(streets), "strassen_fehlend": missing_streets, "ausserhalb_radius": ausserhalb,
            "osm_ok": osm is not None}
    return out, stat


def write_outputs(alle, stats, outdir):
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.utils import get_column_letter
    outdir.mkdir(parents=True, exist_ok=True)
    for stadt, rows in alle.items():
        fn = outdir / f"{STAEDTE[stadt]['kt']}_{re.sub(r'[^A-Za-z0-9äöüéÄÖÜ]+', '_', stadt).strip('_')}_EGID.csv"
        with open(fn, "w", newline="", encoding="utf-8-sig") as fh:
            w = csv.DictWriter(fh, fieldnames=COLS, delimiter=";")
            w.writeheader()
            w.writerows(rows)
    wb = Workbook()
    ws = wb.active
    ws.title = "Übersicht"
    hdr = ["Stadt", "Kanton", "Strassen", "Adressen", "mit EGID", "ohne EGID", "mit EGRID", "Parzellen (eindeutig)",
           "Eigentümer bekannt (Adressen)", "Parzellen noch abzufragen", "nicht in OSM", "Strassen ohne Treffer",
           "ausserhalb Radius (verworfen)"]
    ws.append([f"EGID/EGRID Highstreets – Stand {STAND} – Quelle: GWR (BFS) und amtliche Vermessung via api3.geo.admin.ch"])
    ws.append([])
    ws.append(hdr)
    for c in ws[3]:
        c.font = Font(bold=True, color="FFFFFF")
        c.fill = PatternFill("solid", fgColor="111111")
    for stadt, rows in alle.items():
        st = stats[stadt]
        bekannt = [r for r in rows if r["Eigentümer bekannt (Retail Map)"] or r["Eigentümer-Register 05.11."]]
        bek_par = {r["EGRID"] for r in bekannt if r["EGRID"]}
        par = {r["EGRID"] for r in rows if r["EGRID"]}
        ws.append([stadt, STAEDTE[stadt]["kt"], st["strassen"], len(rows), sum(1 for r in rows if r["EGID"]),
                   sum(1 for r in rows if not r["EGID"]), sum(1 for r in rows if r["EGRID"]), len(par), len(bekannt),
                   len(par - bek_par), sum(1 for r in rows if r["In OSM"] == "nein"), ", ".join(st["strassen_fehlend"]),
                   st["ausserhalb_radius"]])
    ws.append([])
    for t in ["Lesehilfe:",
              "Eine Zeile = eine Gebäudeadresse. Abfrage = «ja» nur für die erste Adresse je Parzelle (EGRID); die übrigen «gleiche Parzelle wie …» brauchen keine eigene Auskunft.",
              "Grün = Eigentümer schon in der Retail Map (SEED) oder im Eigentümer-Register 05.11.2026 erfasst.",
              "Spalten Eigentümer / Datum Auskunft / Quelle sind leer zum Ausfüllen (Quelle z.B. «GRUDIS 06.11.26», «Extrait foncier GE»).",
              "Prio 1 = Toplagen (Top-Strassen + von Kaito genannte Strassen), Prio 2 = weitere Strassen aus der Retail-Map-Ortskonfiguration.",
              "EGRID/Parzelle aus der amtlichen Vermessung (ÖREB-Layer) am Gebäudepunkt; weicht das GWR ab, steht es in «Hinweis». «Weitere Rechte am Punkt» = Baurechte/selbständige Rechte auf derselben Fläche.",
              "Retail-Map-Key: stadt|strasse|hausnummer klein, Strasse wie OSM addr:street. «In OSM = nein» heisst: der Key erscheint in der Karte nur über EXTRA."]:
        ws.append([t])
    ws.column_dimensions["A"].width = 22
    for i in range(2, len(hdr) + 1):
        ws.column_dimensions[get_column_letter(i)].width = 14
    ws.column_dimensions["L"].width = 40
    green = PatternFill("solid", fgColor="E2F0D9")
    widths = {"Strasse": 24, "Retail-Map-Key": 34, "EGRID": 17, "Parzelle": 20, "Mieter (OSM)": 28,
              "Eigentümer bekannt (Retail Map)": 32, "Eigentümer-Register 05.11.": 32, "Hinweis": 40,
              "Link Eigentümerauskunft": 40, "Link ÖREB-Auszug": 30, "Link Karte": 24, "Eigentümer": 30,
              "Datum Auskunft": 14, "Quelle": 20, "Weitere Rechte am Punkt": 30, "Abfrage": 26, "Adressquelle": 18,
              "Gebäudekategorie": 24, "Gebäudeklasse": 20}
    for stadt, rows in alle.items():
        w = wb.create_sheet(stadt[:31].replace("(", "").replace(")", ""))
        w.append(COLS)
        for c in w[1]:
            c.font = Font(bold=True, color="FFFFFF")
            c.fill = PatternFill("solid", fgColor="111111")
            c.alignment = Alignment(wrap_text=True, vertical="top")
        for r in rows:
            w.append([r[c] for c in COLS])
            if r["Eigentümer bekannt (Retail Map)"] or r["Eigentümer-Register 05.11."]:
                for c in w[w.max_row]:
                    c.fill = green
            for cn in ("Link Eigentümerauskunft", "Link ÖREB-Auszug", "Link Karte"):
                v = r[cn]
                if v.startswith("http"):
                    cell = w.cell(row=w.max_row, column=COLS.index(cn) + 1)
                    cell.hyperlink = v.split(" ")[0]
                    cell.font = Font(color="0563C1", underline="single")
        for i, c in enumerate(COLS, 1):
            w.column_dimensions[get_column_letter(i)].width = widths.get(c, 11)
        w.freeze_panes = "E2"
        w.auto_filter.ref = f"A1:{get_column_letter(len(COLS))}{w.max_row}"
    fx = outdir / f"EGID_Highstreets_{STAND}.xlsx"
    wb.save(fx)
    return fx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--staedte", default=",".join(STAEDTE))
    ap.add_argument("--out", default=str(Path.home() / "Downloads/Nachtarbeit_05.11.2026/2_EGID_Highstreets"))
    args = ap.parse_args()
    (TOOLS / "logs").mkdir(exist_ok=True)
    CACHE_F.parent.mkdir(exist_ok=True)
    logf = open(TOOLS / "logs" / f"egid_highstreets_{STAND}.log", "a")

    def log(*a):
        line = time.strftime("%T ") + " ".join(map(str, a))
        print(line, flush=True)
        print(line, file=logf, flush=True)

    sd, reg, cache, cst = seed.load(), load_register(), load_cache(), cities_streets()
    alle, stats = {}, {}
    for stadt in [s.strip() for s in args.staedte.split(",") if s.strip()]:
        rows, st = run_city(stadt, STAEDTE[stadt], cst, sd, reg, cache, log)
        CACHE_F.write_text(json.dumps(cache))
        alle[stadt], stats[stadt] = rows, st
        log(f"  {stadt}: {len(rows)} Adressen, {sum(1 for r in rows if r['EGID'])} mit EGID, "
            f"{len({r['EGRID'] for r in rows if r['EGRID']})} Parzellen, ausserhalb Radius {st['ausserhalb_radius']}")
    fx = write_outputs(alle, stats, Path(args.out).expanduser())
    json.dump(stats, open(Path(args.out).expanduser() / "lauf_statistik.json", "w"), ensure_ascii=False, indent=1)
    log("fertig:", fx)


if __name__ == "__main__":
    main()
