"""Ermittelt pro Gemeinde die stärksten Geschäftsstrassen aus OSM (Anzahl Läden/Gastro/Dienstleister mit addr:street)."""
import json, sys, time, urllib.parse, urllib.request, collections

UA = {"User-Agent": "kuroiwa-retailmap/1.0"}
EPS = ["https://overpass.osm.ch/api/interpreter", "https://overpass-api.de/api/interpreter"]

def get(url, data=None):
    req = urllib.request.Request(url, data=data, headers=UA)
    with urllib.request.urlopen(req, timeout=180) as r: return json.load(r)

def zentrum(gemeinde):
    """Ortszentrum (place-Node bzw. Mittelpunkt) der Gemeinde, nicht des gleichnamigen Kantons."""
    if "@" in gemeinde:  # "Name@lat,lon" als manuelle Vorgabe
        n, c = gemeinde.split("@"); la, lo = c.split(","); return float(la), float(lo), n
    r = overpass(f'[out:json][timeout:60];area["ISO3166-1"="CH"]->.ch;node(area.ch)["place"~"^(city|town|village)$"]["name"="{gemeinde}"];out;')
    pl = sorted(r["elements"], key=lambda e: ["city", "town", "village"].index(e["tags"]["place"]))
    if pl: return pl[0]["lat"], pl[0]["lon"], gemeinde + " (" + pl[0]["tags"]["place"] + ")"
    q = urllib.parse.quote(gemeinde)
    hits = get(f"https://nominatim.openstreetmap.org/search?format=jsonv2&limit=5&countrycodes=ch&featureType=settlement&q={q}")
    if not hits: raise SystemExit(f"Ort {gemeinde} nicht gefunden")
    h = hits[0]; return float(h["lat"]), float(h["lon"]), h["display_name"]

def overpass(q):
    for ep in EPS:
        try: return get(ep, urllib.parse.urlencode({"data": q}).encode())
        except Exception as e: err = e; time.sleep(3)
    raise err

def top(gemeinde, n=5, radius=900):
    lat, lon, name = zentrum(gemeinde)
    a = f"around:{radius},{lat},{lon}"
    q = f"""[out:json][timeout:120];
(nwr({a})["shop"]["addr:street"];nwr({a})["amenity"~"^(restaurant|cafe|bar|bank|pharmacy|fast_food)$"]["addr:street"];);out tags;"""
    els = overpass(q)["elements"]
    shops = collections.Counter(); alle = collections.Counter()
    for e in els:
        t = e.get("tags", {}); s = t["addr:street"]
        alle[s] += 1
        if "shop" in t and t["shop"] not in ("vacant", "car", "car_repair", "kiosk"): shops[s] += 1
    # Gewichtung: Läden doppelt, Gastro/Bank einfach
    score = {s: 2 * shops[s] + (alle[s] - shops[s]) for s in alle}
    rang = sorted(score, key=lambda s: -score[s])
    return name, [(s, shops[s], alle[s]) for s in rang[:n]]

if __name__ == "__main__":
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    rad = int(sys.argv[3]) if len(sys.argv) > 3 else 900
    name, r = top(sys.argv[1], n, rad)
    print(name)
    for s, a, b in r: print(f"  {s}: {a} Läden, {b} total")
