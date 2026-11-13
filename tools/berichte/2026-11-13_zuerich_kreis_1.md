# Folgelauf 13.11.2026: Zürich (Kreis 1), Eigentümer

- Strassen unverändert: Bahnhofstrasse, Rennweg, Löwenstrasse, Limmatquai, Niederdorfstrasse (330 Adressen im SEED, keine neuen Mieter, da Folgelauf).
- Stand: 146 von 330 Adressen mit Eigentümer, offen 184 (Limmatquai 57, Niederdorfstrasse 50, Rennweg 38, Löwenstrasse 37, Bahnhofstrasse 1, Kämbelgasse 1). Bahnhofstrasse ist bis auf Nr. 16 (online gesperrt) vollständig.
- Register-Abgleich (134 Dateien): 0 neue Eigentümer, 0 neue Hinweise; 684 bestätigt, 12 Konflikte (gesamte Schweiz, siehe 2026-11-13_register_abgleich.csv, nicht committet).
- Parzelle neu: Limmatquai 140 (Central Jewellery) hat keine amtliche Adresse; per OSM-Koordinate Parzelle AA6234, E-GRID CH559199779123, gleiche Parzelle wie Niederdorfstrasse 77. Alle offenen Adressen haben jetzt Parzelle und E-GRID.
- Websuche (Rennweg, Löwenstrasse, Limmatquai): nur Mietinserate, keine belastbaren neuen Eigentümer. Nichts eingetragen.
- Anfrageliste neu je Parzelle mit Direktlink (portal.objektwesen.zh.ch/aks/detail?egrid=…&bfsNr=261): tools/anfragen/ZH_Zürich (Kreis 1).csv (154 Parzellen, Prioritaet 1: 41, 2: 101, 3: 12) plus _Anleitung.txt. Nicht committet; Kaito muss sie nach ~/Downloads/Retail Map Anfragen/ kopieren. Limit 5 pro Tag.

## Probleme
- ~/Downloads im launchd-Lauf wieder gesperrt (PermissionError, `ls` hängt). antworten_einlesen.py ist am Start abgebrochen: Antworten in ~/Downloads/Retail Map Anfragen/Antworten/ wurden NICHT eingelesen, `_nicht_zugeordnet_*.csv` konnten nicht gelesen werden. register_abgleich.py lief mit HOME=/tmp/rmhome (ohne Parzellen-CSVs aus Downloads).
- git pull im Tageslauf scheiterte wegen ungestagter Änderungen im Arbeitsbaum.
