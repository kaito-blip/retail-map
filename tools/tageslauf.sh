#!/bin/zsh
# Täglicher Retail-Map-Lauf: nächste Stadt aus staedte.json, Strassen + Eigentümer, Commit/Push.
export PATH="/Users/kaito/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
cd /Users/kaito/retail-map || exit 1
LOCK=/tmp/retailmap-tageslauf.lock
# Mit Stadt-Argument: warten, bis ein laufender Lauf fertig ist; ohne: überspringen
while [ -e $LOCK ] && kill -0 $(cat $LOCK) 2>/dev/null; do [ -z "$1" ] && { echo "läuft schon"; exit 0; }; sleep 60; done
echo $$ > $LOCK; trap 'rm -f $LOCK' EXIT
TAG=$(date +%F)
LOG=tools/logs/$TAG.log
git pull -q --rebase >>$LOG 2>&1
# Antworten aus «Retail Map Anfragen/Antworten/» eintragen (nur CSV; Zeitlimit, weil launchd bei Downloads hängen kann)
perl -e 'alarm 180; exec @ARGV' python3 tools/antworten_einlesen.py >>$LOG 2>&1
STADT="$1"
[ -z "$STADT" ] && STADT=$(python3 - <<'PY'
import json
s=json.load(open("tools/staedte.json"))
neu=[x for x in s if not x["letzter_lauf"]]
alt=sorted([x for x in s if x["letzter_lauf"] and x.get("offen")!="0"], key=lambda x:x["letzter_lauf"])
print((neu or alt or s)[0]["stadt"])
PY
)
echo "=== $TAG $(date +%T) Stadt: $STADT" >>$LOG
AUFTRAG="$(cat tools/tagesauftrag.md)

HEUTIGE STADT: $STADT
DATUM: $TAG"
caffeinate -i claude -p "$AUFTRAG" --dangerously-skip-permissions --model opus >>$LOG 2>&1
echo "=== Ende $(date +%T)" >>$LOG
