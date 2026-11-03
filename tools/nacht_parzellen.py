"""Nachtlauf: für alle Städte aus staedte.json Top-5-Strassen, alle Adressen, EGID, Parzelle, E-GRID → CSV je Stadt.
Schreibt NICHT in index.html. Fortsetzbar: Städte mit vorhandener CSV werden übersprungen."""
import csv, json, re, sys, time, traceback
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import seed, parzelle, adressen, topstrassen

OUT = Path.home() / "Downloads/Retail Map Anfragen/Parzellen"; OUT.mkdir(parents=True, exist_ok=True)
html = (Path(__file__).parent.parent / "index.html").read_text()
cities = {m.group(1): re.findall(r"'((?:[^'\\]|\\.)*)'", m.group(2))
          for m in re.finditer(r"^ '([^']+)': \{q:'[^']*', streets:\[(.*?)\]\}", html, re.M)}
log = open(Path(__file__).parent / "logs" / f"nacht_{time.strftime('%F')}.log", "a")
def L(*a): print(time.strftime("%T"), *a, file=log, flush=True)

def strassen_fuer(st):
    if st["strassen"]: return st["strassen"]
    _, rang = topstrassen.top(st["ort"], 25, st["radius"])
    rang = [r[0] for r in rang]
    conf = [s.replace("\\'", "'") for s in cities.get(st["stadt"], [])]
    wahl = [s for s in rang if s in conf][:5]
    for s in rang:
        if len(wahl) >= 5: break
        if s not in wahl: wahl.append(s)
    return wahl

d = seed.load()
for st in json.load(open(Path(__file__).parent / "staedte.json")):
    fn = OUT / f"{st['kanton']}_{re.sub(r'[^A-Za-z0-9äöüéèàÄÖÜ]+', '_', st['stadt']).strip('_')}.csv"
    if fn.exists(): continue
    try:
        strassen = strassen_fuer(st); time.sleep(5)
        L(st["stadt"], "Strassen:", strassen)
        ortq = st["ort"].split("@")[0]
        adressen.run(st["stadt"], st["ort"], strassen)
        a = json.load(open(Path(__file__).parent / "adressen" / f"{re.sub(r'[^a-z0-9]+','_',st['stadt'].lower())}.json"))
        gefunden = {v["street"] for v in a.values()}
        fehlt = [s for s in strassen if s not in gefunden]
        if fehlt:  # Strassenname passt nicht zu OSM → durch nächstbeste Ladenstrasse ersetzen
            _, rang = topstrassen.top(st["ort"], 15, st["radius"])
            ersatz = [r[0] for r in rang if r[0] not in strassen]
            strassen = [s for s in strassen if s in gefunden] + ersatz[:len(fehlt)]
            L(st["stadt"], "nicht in OSM:", fehlt, "→ ersetzt, neu:", strassen)
            adressen.run(st["stadt"], st["ort"], strassen)
        a = json.load(open(Path(__file__).parent / "adressen" / f"{re.sub(r'[^a-z0-9]+','_',st['stadt'].lower())}.json"))
        rows = []
        for k, v in sorted(a.items(), key=lambda kv: (strassen.index(kv[1]["street"]) if kv[1]["street"] in strassen else 99, kv[1]["hn"])):
            p = None
            for _ in range(3):
                try: p = parzelle.parzelle(f"{v['street']} {v['hn']}", ortq); break
                except Exception: time.sleep(5)
            p = p or {}
            rows.append([v["street"], v["hn"], p.get("egid", ""), p.get("parzelle", ""), p.get("egrid", ""),
                         " · ".join(v["mieter"]), d.get(k, {}).get("owner", ""), ""])
            time.sleep(0.3)
        tmp = fn.with_suffix(".tmp")
        with open(tmp, "w", newline="") as fh:
            w = csv.writer(fh, delimiter=";")
            w.writerow(["Strasse", "Nr", "EGID", "Parzelle", "E-GRID", "Mieter (OSM)", "Eigentuemer bekannt", "Eigentuemer"])
            w.writerows(rows)
        tmp.rename(fn)
        L(st["stadt"], len(rows), "Adressen,", sum(1 for r in rows if r[3]), "mit Parzelle")
    except Exception:
        L(st["stadt"], "FEHLER", traceback.format_exc().splitlines()[-1])
    time.sleep(10)
L("fertig")
