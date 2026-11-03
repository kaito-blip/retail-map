"""Alle Adressen + Laden-POIs auf den Strassen einer Stadt (Overpass), Ausgabe JSON nach tools/adressen/<stadt>.json."""
import json, re, sys, collections
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from topstrassen import overpass, zentrum

def run(stadt, ort, strassen, radius=2500):
    lat, lon, _ = zentrum(ort)
    rx = "^(" + "|".join(re.escape(s) for s in strassen) + ")$"
    q = f"""[out:json][timeout:180];nwr(around:{radius},{lat},{lon})["addr:street"~"{rx}"]["addr:housenumber"];out center tags;"""
    adr = {}
    for e in overpass(q)["elements"]:
        t = e["tags"]; key = f"{stadt.lower()}|{t['addr:street'].lower()}|{t['addr:housenumber'].lower()}"
        c = e.get("center") or e
        a = adr.setdefault(key, {"street": t["addr:street"], "hn": t["addr:housenumber"], "lat": c.get("lat"), "lng": c.get("lon"), "mieter": []})
        name = t.get("brand") or t.get("name")
        if name and ("shop" in t or "amenity" in t or "office" in t or "craft" in t):
            if name not in a["mieter"]: a["mieter"].append(name)
    out = Path(__file__).parent / "adressen"; out.mkdir(exist_ok=True)
    (out / f"{re.sub(r'[^a-z0-9]+','_',stadt.lower())}.json").write_text(json.dumps(adr, ensure_ascii=False, indent=1))
    c = collections.Counter(v["street"] for v in adr.values())
    print(len(adr), "Adressen,", sum(1 for v in adr.values() if v["mieter"]), "mit Mieter-POI;", dict(c))

if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2], sys.argv[3].split(";"))
