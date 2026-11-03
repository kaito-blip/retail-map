"""Parzelle + E-GRID zu einer Adresse über api3.geo.admin.ch. Aufruf: parzelle.py "Marktgasse 20" "8400 Winterthur"|Winterthur"""
import json, re, sys, urllib.parse, urllib.request

def _get(u):
    with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "kuroiwa-retailmap/1.0"}), timeout=30) as r:
        return json.load(r)

def parzelle(adresse, ort):
    q = urllib.parse.quote(f"{adresse} {ort}")
    res = _get(f"https://api3.geo.admin.ch/rest/services/api/SearchServer?type=locations&origins=address&sr=2056&searchText={q}")["results"]
    pat = re.compile(r"^" + re.escape(adresse) + r"\b", re.I)
    hit = next((r for r in res if pat.match(re.sub("<[^>]+>", "", r["attrs"]["label"]))), None)
    if not hit: return None
    e, n = hit["attrs"]["y"], hit["attrs"]["x"]  # geo.admin: y = Ost, x = Nord
    idf = _get("https://api3.geo.admin.ch/rest/services/api/MapServer/identify?geometryType=esriGeometryPoint"
               f"&geometry={e},{n}&sr=2056&layers=all:ch.kantone.cadastralwebmap-farbe&tolerance=0&returnGeometry=false")["results"]
    if not idf: return {"label": hit["attrs"]["label"], "e": e, "n": n}
    a = idf[0]["attributes"]
    return {"label": re.sub("<[^>]+>", "", hit["attrs"]["label"]), "kanton": a["ak"], "parzelle": a["number"],
            "egrid": a["egris_egrid"], "e": e, "n": n, "geoportal": a.get("geoportal_url")}

if __name__ == "__main__":
    print(json.dumps(parzelle(sys.argv[1], sys.argv[2]), ensure_ascii=False))
