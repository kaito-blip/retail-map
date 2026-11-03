"""SEED der Retail Map sicher lesen, ergänzen und zurückschreiben (mit JS-Syntaxprüfung)."""
import json, subprocess, sys
from pathlib import Path

HTML = Path(__file__).resolve().parent.parent / "index.html"
FIELDS = ["owner","ownerType","ownerAddr","ownerEmail","ownerPhone","ownerUid","ownerSince","parcel",
          "contact","mgmt","mgmtContact","tenant","area","area2","rate","rent","leaseEnd","buildYear",
          "price","status","notes","updated"]

def _split(s):
    i = s.index("var SEED = ") + len("var SEED = ")
    d, n = json.JSONDecoder(strict=False).raw_decode(s[i:])
    return s[:i], d, s[i + n:]

def load():
    return _split(HTML.read_text())[1]

def js_ok(s):
    a = s.index("<script>", s.index("leaflet.js")); b = s.index("</script>", a)
    p = Path("/tmp/retailmap_check.js"); p.write_text(s[a + 8:b])
    js = ('ObjC.import("Foundation");var t=$.NSString.stringWithContentsOfFileEncodingError("%s",4,null).js;'
          'try{new Function(t);"OK"}catch(e){"FEHLER "+e.message}' % p)
    r = subprocess.run(["osascript", "-l", "JavaScript", "-e", js], capture_output=True, text=True)
    return r.stdout.strip() == "OK", r.stdout.strip() + r.stderr.strip()

def save(d):
    s = HTML.read_text()
    pre, _, post = _split(s)
    new = pre + json.dumps(d, ensure_ascii=False, separators=(",", ":")) + post
    ok, msg = js_ok(new)
    if not ok:
        sys.exit("JS-Prüfung fehlgeschlagen, nichts geschrieben: " + msg)
    HTML.write_text(new)

def merge(d, key, rec, stamp):
    """Ergänzt nur leere Felder; überschreibt nichts Bestehendes. Gibt True zurück, wenn etwas neu ist."""
    cur = d.get(key) or {f: "" for f in FIELDS}
    changed = False
    for f, v in rec.items():
        if f in FIELDS and v and not cur.get(f):
            cur[f] = v; changed = True
    if changed:
        for f in FIELDS: cur.setdefault(f, "")
        if cur.get("owner") and cur.get("status") in ("", "offen"): cur["status"] = "erfasst"
        cur["status"] = cur["status"] or "offen"
        cur["updated"] = stamp
        d[key] = cur
    return changed

if __name__ == "__main__":
    import collections
    d = load()
    if "--fix" in sys.argv:
        save(d); print("SEED neu serialisiert,", len(d), "Einträge")
    c = collections.Counter(k.split("|")[0] for k in d)
    o = collections.Counter(k.split("|")[0] for k, v in d.items() if v.get("owner"))
    print(len(d), "Einträge,", sum(o.values()), "mit Eigentümer")
    for k, v in c.most_common(): print(f"  {k}: {v} ({o[k]} Eigentümer)")
