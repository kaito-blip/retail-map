"""Eigentümer-Register (tools/eigentuemer_register/*.csv) mit den Adressen der Retail Map abgleichen.

Aufruf:
  python3 tools/register_abgleich.py            # nur Bericht (Trockenlauf)
  python3 tools/register_abgleich.py --schreiben  # SEED ergänzen + Parzellen-CSVs nachführen

Quellen der Retail-Map-Adressen: SEED (index.html) und ~/Downloads/Retail Map Anfragen/Parzellen/<KT>_<Stadt>.csv.
merge überschreibt nie: vorhandene owner bleiben, abweichende Register-Treffer kommen nur in die Konfliktliste.
"""
import csv, json, re, sys, unicodedata, collections, datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import seed

TOOLS = Path(__file__).resolve().parent
REG = TOOLS / "eigentuemer_register"
PARZ = Path.home() / "Downloads/Retail Map Anfragen/Parzellen"
STAMP = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")

# Ortsbezeichnungen aus Berichten -> Retail-Map-Stadt(e)
ALIAS = {
    "zurich": ["Zürich (Kreis 1)", "Zürich (übrige Kreise)"], "zuerich": ["Zürich (Kreis 1)", "Zürich (übrige Kreise)"],
    "geneve": ["Genf"], "genf": ["Genf"], "geneva": ["Genf"], "ginevra": ["Genf"],
    "biel": ["Biel/Bienne"], "bienne": ["Biel/Bienne"], "biel/bienne": ["Biel/Bienne"], "biel-bienne": ["Biel/Bienne"],
    "fribourg": ["Fribourg"], "freiburg": ["Fribourg"], "neuchatel": ["Neuchâtel"], "neuenburg": ["Neuchâtel"],
    "sion": ["Sion"], "sitten": ["Sion"], "lucerne": ["Luzern"], "lugano": ["Lugano"], "berne": ["Bern"],
    "bale": ["Basel"], "basilea": ["Basel"], "saanen": ["Gstaad"], "gstaad": ["Gstaad"],
    "st. moritz": ["St. Moritz"], "st.moritz": ["St. Moritz"], "sankt moritz": ["St. Moritz"], "san murezzan": ["St. Moritz"],
    "st. gallen": ["St. Gallen"], "st.gallen": ["St. Gallen"], "sankt gallen": ["St. Gallen"], "saint-gall": ["St. Gallen"],
    "rapperswil-jona": ["Rapperswil"], "jona": ["Rapperswil"], "pfaffikon": ["Pfäffikon SZ"], "freienbach": ["Pfäffikon SZ"],
    "pfaffikon sz": ["Pfäffikon SZ"], "brig-glis": ["Brig"], "glis": ["Brig"], "buchs sg": ["Buchs SG"], "buchs": ["Buchs SG"],
    "wil sg": ["Wil"], "montana": ["Crans-Montana"], "crans": ["Crans-Montana"], "verbier": ["Verbier"], "bagnes": ["Verbier"],
    "val de bagnes": ["Verbier"], "davos platz": ["Davos"], "davos dorf": ["Davos"], "klosters-serneus": ["Klosters"],
    "yverdon": ["Yverdon-les-Bains"], "la chaux-de-fonds": ["La Chaux-de-Fonds"], "delemont": ["Delémont"],
    "carouge ge": ["Carouge"], "baden ag": ["Baden"], "wohlen ag": ["Wohlen"], "rheinfelden ag": ["Rheinfelden"],
    "montreux-clarens": ["Montreux"], "clarens": ["Montreux"], "territet": ["Montreux"],
    "lugano-paradiso": [], "paradiso": [], "muralto": ["Locarno"], "minusio": [],
    "zug": ["Zug"], "chur": ["Chur"], "coire": ["Chur"], "thoune": ["Thun"], "soleure": ["Solothurn"],
    "schaffhouse": ["Schaffhausen"], "argovie": [], "winterthour": ["Winterthur"],
}


def norm(s):
    s = re.sub(r"[\u2010-\u2015\u2212]", "-", str(s or "")).replace("ß", "ss").replace("’", "'")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower().strip()
    s = re.sub(r"\bstr\.?(?=\s|$)", "strasse", s)
    s = re.sub(r"(?<=[a-z])str\.?$", "strasse", s)
    s = re.sub(r"\b(?:st(?:\.\s*|\s+)|sankt\s+)", "st. ", s)
    s = s.replace("’", "'").replace("`", "'")
    s = re.sub(r"[\-‐–—]", "-", s)
    s = re.sub(r"\s+", " ", s).strip(" ,.")
    return s


TYPES = r"^(rue|avenue|boulevard|place|chemin|route|via|viale|piazza|quai|corso|vicolo|contrada|ruelle|passage|promenade|grandrue)"


def norm_street(s):
    s = norm(s)
    s = re.sub(r"\s*-\s*", "-", s)
    s = s.replace("'", " ").replace("-", " ")
    s = re.sub(r"\b(rue|avenue|av\.|boulevard|bd|place|pl\.|chemin|ch\.|route|rte|via|viale|piazza|quai)\b",
               lambda m: {"av.": "avenue", "bd": "boulevard", "pl.": "place", "ch.": "chemin", "rte": "route"}.get(m.group(1), m.group(1)), s)
    s = re.sub(r"\b(de la|de l|du|des|de|d|la|le|les|l|dal|da|del|della)\b", " ", s)
    return re.sub(r"\s+", "", s)


def expand_nr(nr):
    """'10/12' -> 10,12 · '48-52' -> 48,50,52 · '3, 5' · '12a' · '7-7a'"""
    nr = norm(nr).replace(" und ", ",").replace(" et ", ",").replace("+", ",").replace(";", ",").replace("&", ",")
    out = []
    for part in re.split(r"[,/]", nr):
        part = part.strip()
        if not part: continue
        m = re.fullmatch(r"(\d+)\s*([a-z]?)\s*-\s*(\d+)\s*([a-z]?)", part)
        if m:
            a, b = int(m.group(1)), int(m.group(3))
            if a == b:
                out += [m.group(1) + m.group(2), m.group(3) + m.group(4)]
            elif 0 < b - a <= 20:
                step = 1 if b - a == 1 else 2
                if (b - a) % 2: step = 1
                out += [str(x) for x in range(a, b + 1, step)]
            else:
                out += [str(a), str(b)]
            continue
        m = re.fullmatch(r"(\d+)\s*([a-z]?)(\s*-\s*[a-z])?", part)
        if m:
            out.append(m.group(1) + m.group(2))
    return list(dict.fromkeys(out))


def ort_targets(ort, plz, staedte_by_norm):
    o = norm(ort)
    o = re.sub(r"\s*\((?:[a-z]{2}|kanton.*)\)$", "", o).strip()
    o2 = re.sub(r"\s+(zh|be|lu|ur|sz|ow|nw|gl|zg|fr|so|bs|bl|sh|ar|ai|sg|gr|ag|tg|ti|vd|vs|ne|ge|ju)$", "", o)
    for cand in (o, o2, o.split(" ")[0] if o else ""):
        if cand in ALIAS: return ALIAS[cand]
        if cand in staedte_by_norm: return [staedte_by_norm[cand]]
    return []


def lade_retailmap():
    st = json.load(open(TOOLS / "staedte.json"))
    by_norm = {norm(c["stadt"]): c["stadt"] for c in st}
    for c in st: by_norm.setdefault(norm(c["ort"].split("@")[0]), c["stadt"])
    kt = {c["stadt"]: c["kanton"] for c in st}
    seed_d = seed.load()
    idx = {}  # (stadt, street_norm, nr) -> dict(key, strasse, nr, parzelle, egrid, csv)
    stadt_of_key = {c["stadt"].lower(): c["stadt"] for c in st}
    for k in seed_d:
        s, strasse, nr = k.split("|")
        stadt = stadt_of_key.get(s)
        if not stadt: continue
        e0 = {"key": k, "strasse": strasse, "nr": nr}
        for alt in [strasse] + strasse.split("/"):
            idx.setdefault((stadt, norm_street(alt), nr.lower()), e0)
    for c in st:
        f = PARZ / (c["kanton"] + "_" + re.sub(r"[^A-Za-z0-9äöüÄÖÜéèàç]+", "_", c["stadt"]).strip("_") + ".csv")
        if not f.exists():
            cands = [p for p in PARZ.glob(c["kanton"] + "_*.csv")
                     if norm(p.stem[3:].replace("_", " ")) == norm(re.sub(r"[^\w]+", " ", c["stadt"]))]
            if not cands: continue
            f = cands[0]
        for r in csv.DictReader(open(f, encoding="utf-8"), delimiter=";"):
            key = (c["stadt"], norm_street(r["Strasse"]), r["Nr"].strip().lower())
            e = idx.setdefault(key, {"key": f"{c['stadt'].lower()}|{r['Strasse'].lower()}|{r['Nr'].strip().lower()}",
                                     "strasse": r["Strasse"], "nr": r["Nr"].strip()})
            for alt in r["Strasse"].split("/")[1:] + r["Strasse"].split("/")[:1]:
                idx.setdefault((c["stadt"], norm_street(alt), r["Nr"].strip().lower()), e)
            e.update({"parzelle": r.get("Parzelle", ""), "egrid": r.get("E-GRID", ""), "csv": f,
                      "mieter": r.get("Mieter (OSM)", "")})
    return st, by_norm, kt, seed_d, idx


TYP = {"Fonds": "Immobilienfonds", "AG": "Immobilien-AG/Firma", "AST": "Pensionskasse/Anlagestiftung",
       "PK": "Pensionskasse/Anlagestiftung", "OEFF": "öffentliche Hand"}


def owner_type(row):
    e = (row["eigentuemer"] + " " + row["vehikel"]).lower()
    if "unbestätigt" in (row.get("anteil") or "").lower(): return None
    if re.search(r"stadt |ville de|etat de|kanton|canton|gemeinde|commune|città|burgergemeinde|korporation|einwohnergemeinde", e): return "Öffentliche Hand"
    if re.search(r"\bsbb\b|post immobilien|schweizerische post", e): return "Öffentliche Hand"
    if re.search(r"fund|fonds|sicav|property fund|immo pk|immoplus|foncipars|sima|anfos|swissreal|la fonci", e): return "Fonds/Anlagestiftung"
    if re.search(r"anlagestiftung|fondation de placement", e): return "Fonds/Anlagestiftung"
    if re.search(r"pensionskasse|caisse de pr|prévoyance|cpeg|bvk|publica|vorsorge", e): return "Pensionskasse"
    if re.search(r"stiftung|fondation", e): return "Stiftung"
    if re.search(r"\bzunft\b|constaffel|genossenschaft zum r", e): return ""  # Zunft/Verein: kein passender Formularwert
    if re.search(r"versicherung|assurance|insurance|swiss life|baloise|helvetia|mobiliar|allianz|axa leben", e): return "Versicherung"
    return "Immobilien-AG/Firma"


def lade_register():
    rows = []
    for f in sorted(REG.glob("*.csv")):
        try:
            for r in csv.DictReader(open(f, encoding="utf-8-sig"), delimiter=";"):
                if not r.get("strasse") or not r.get("ort") and not r.get("plz"): continue
                r["_datei"] = f.name
                r["eigentuemer"] = re.sub(r"\s*\(ABGELEITET[^)]*\)", "", r["eigentuemer"]).strip()
                if r["_datei"] == "burgergemeinde_bern.csv": r["anteil"] = ((r.get("anteil") or "") + " unbestätigt").strip()
                rows.append(r)
        except Exception as ex:
            print("Datei nicht lesbar:", f.name, ex)
    return rows


def main(schreiben):
    st, by_norm, kt, d, idx = lade_retailmap()
    rows = lade_register()
    print(len(rows), "Registerzeilen aus", len({r['_datei'] for r in rows}), "Dateien;", len(idx), "Retail-Map-Adressen")
    treffer = collections.defaultdict(list)
    streets = collections.defaultdict(set)
    for (c_, s_, n_) in idx: streets[c_].add(s_)
    ohne_ort = collections.Counter()
    for r in rows:
        ziele = ort_targets(r.get("ort", ""), r.get("plz", ""), by_norm)
        # Kanton muss passen: sonst landet z.B. «Pfäffikon ZH» über den Alias «pfaffikon» bei Pfäffikon SZ
        # (nur Kantonszusatz im Ortsnamen zählt; die Spalte kanton ist in einzelnen Registern falsch, z.B. Davos «VS»)
        m_kt = re.search(r"[\s(](zh|be|lu|ur|sz|ow|nw|gl|zg|fr|so|bs|bl|sh|ar|ai|sg|gr|ag|tg|ti|vd|vs|ne|ge|ju)\)?$", norm(r.get("ort", "")))
        if m_kt: ziele = [z for z in ziele if kt.get(z, m_kt.group(1).upper()) == m_kt.group(1).upper()]
        if not ziele:
            ohne_ort[r.get("ort", "")] += 1; continue
        for stadt in ziele:
            sns = [norm_street(a) for a in r["strasse"].split(" / ")]
            if not re.match(TYPES, sns[0]):  # z.B. FIR: «Gare 5» ohne Strassentyp
                cores = {x for x in streets[stadt] if re.sub(TYPES, "", x) == sns[0]}
                if len(cores) == 1: sns.append(cores.pop())
            for nr in expand_nr(r.get("nr", "")):
                for sn in sns:
                    e = idx.get((stadt, sn, nr))
                    if e: treffer[e["key"]].append((r, e)); break
    print(len(treffer), "Adressen mit Treffer")

    neu, konflikt, gleich, bericht = [], [], [], []
    csv_upd = collections.defaultdict(dict)
    for key, hits in sorted(treffer.items()):
        e = hits[0][1]
        fest = [h for h in hits if "unbestätigt" not in (h[0].get("anteil") or "").lower()]
        if fest: hits = fest
        owners = list(dict.fromkeys(h[0]["eigentuemer"].strip() for h in hits))
        def gruppe(o):
            o = norm(o).replace("anlagestiftung", "").replace("fund management (switzerland) ag", "")
            return re.sub(r"[^a-z]", " ", o).split()[0] if o.strip() else o
        same_group = len({gruppe(o) for o in owners}) == 1
        r = hits[0][0]
        src = "; ".join(dict.fromkeys(f"{h[0]['vehikel']}: {h[0]['dokument']} ({h[0]['stand']})" for h in hits))
        unbest = all("unbestätigt" in (h[0].get("anteil") or "").lower() for h in hits)
        cur = d.get(key, {})
        rec = {"parcel": (e.get("parzelle") and f"{e['parzelle']}") or ""}
        anteil = "; ".join(dict.fromkeys(h[0]["anteil"] for h in hits if h[0].get("anteil")))
        note = f"Eigentümer lt. {src}" + (f", {anteil}" if anteil else "") + (f", E-GRID {e['egrid']}" if e.get("egrid") else "")
        if len(owners) > 1 and same_group:
            owners = [" / ".join(owners)]
        if unbest or len(owners) > 1:
            # mehrere verschiedene Eigentümer oder unbestätigt -> nur Hinweis
            if len(owners) > 1 and not unbest:
                note = "Register mehrdeutig, vermutlich: " + " / ".join(owners) + f" (Quellen: {src}), ungeprüft"
            else:
                note = "vermutlich " + owners[0] + f" (Quelle: {src}), ungeprüft"
            kind = "hinweis"
        else:
            rec["owner"] = owners[0]
            t = owner_type(r)
            if t: rec["ownerType"] = t
            kind = "owner"
        have = (cur.get("owner") or "").strip()
        if kind == "owner" and have:
            if norm(have)[:12] in norm(rec["owner"]) or norm(rec["owner"])[:12] in norm(have):
                gleich.append(key); continue
            konflikt.append((key, have, rec["owner"], src))
            cnote = f"Register nennt abweichend {rec['owner']} (Quelle: {src}); Grundbuch-Eintrag oben bleibt massgebend, ggf. Tochtergesellschaft oder Handänderung prüfen"
            if cnote not in (cur.get("notes") or ""): neu.append((key, "konfliktnotiz", {}, cnote, e))
            continue
        if note in (cur.get("notes") or ""): continue
        neu.append((key, kind, rec, note, e))
        if kind == "owner" and e.get("csv"):
            csv_upd[e["csv"]][(e["strasse"], e["nr"])] = rec["owner"]

    by_kind = collections.Counter(k for _, k, *_ in neu)
    print(f"neu: {by_kind['owner']} Eigentümer, {by_kind['hinweis']} Hinweise · bestätigt (schon gleich): {len(gleich)} · Konflikte: {len(konflikt)}")
    per_city = collections.Counter(k.split("|")[0] for k, kind, *_ in neu if kind == "owner")
    for c, n in per_city.most_common(): print(f"  {c}: {n}")
    if ohne_ort:
        print("Orte ohne Retail-Map-Stadt (Top 15, informativ):", ", ".join(f"{o}({n})" for o, n in ohne_ort.most_common(15)))

    out = TOOLS / "berichte" / f"{STAMP[:10]}_register_abgleich.csv"
    with open(out, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter=";")
        w.writerow(["Art", "Key", "Eigentümer neu", "Eigentümer bisher", "Quelle/Notiz"])
        for key, kind, rec, note, e in neu: w.writerow([kind, key, rec.get("owner", ""), "", note])
        for key, have, new, src in konflikt: w.writerow(["konflikt", key, new, have, src])
        for key in gleich: w.writerow(["bestätigt", key, "", d[key].get("owner"), ""])
    print("Abgleichliste:", out)

    if not schreiben: return
    for key, kind, rec, note, e in neu:
        cur = d.get(key)
        if cur is None and e.get("mieter"): rec["tenant"] = e["mieter"]
        seed.merge(d, key, rec, STAMP)
        cur = d[key] if key in d else None
        if cur is None:
            seed.merge(d, key, {"notes": note}, STAMP); continue
        if note not in (cur.get("notes") or ""):
            cur["notes"] = (cur["notes"] + " | " if cur.get("notes") else "") + note
            cur["updated"] = STAMP
    seed.save(d)
    print("SEED gespeichert:", len(d), "Einträge")
    for f, upd in csv_upd.items():
        rows_ = list(csv.DictReader(open(f, encoding="utf-8"), delimiter=";"))
        fields = list(rows_[0].keys())
        for r in rows_:
            o = upd.get((r["Strasse"], r["Nr"].strip()))
            if o and not r.get("Eigentuemer bekannt") and not r.get("Eigentuemer"):
                r["Eigentuemer bekannt"] = o
        with open(f, "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=fields, delimiter=";"); w.writeheader(); w.writerows(rows_)
    print(len(csv_upd), "Parzellen-CSVs nachgeführt")


if __name__ == "__main__":
    main("--schreiben" in sys.argv)
