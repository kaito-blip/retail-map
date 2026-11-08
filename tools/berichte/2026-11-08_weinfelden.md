# Weinfelden (TG), Lauf 08.11.2026

## Strassen
In CITIES standen schon: Frauenfelderstrasse, Rathausstrasse, Marktplatz, Bahnhofstrasse, Wilerstrasse. Sie bleiben alle drin.
Ergänzt: **Amriswilerstrasse** (laut topstrassen.py gleichauf mit Rathaus- und Frauenfelderstrasse, im Kern Migros und McOptic). Damit stehen 6 Strassen in CITIES, einer mehr als die Vorgabe von 4 bis 5, weil bestehende Einträge nicht entfernt werden.
Ein Filter nach Entfernung vom Zentrum hält die Liste auf den Kern, die äusseren Abschnitte sind Wohn- und Gewerbelagen:
- Frauenfelderstrasse 420 m (bis etwa Nr. 61), Wilerstrasse 450 m (bis Nr. 21), Amriswilerstrasse 350 m (11 Adressen, bis Nr. 24).
- Aus den Rohdaten fallen 108 Adressen weg (264 → 156 → nach Korrektur 155).
- Register-Treffer an der Amriswilerstrasse (UBS Anfos 60-64, UBS Direct Residential 47/49, Helvetica 72, alle Wohnen) liegen ausserhalb des Kerns und sind deshalb nicht erfasst.
staedte.json: `strassen_ok` true.

## Zahlen
- Adressen: 155 (Frauenfelderstrasse 62, Bahnhofstrasse 33, Rathausstrasse 30, Wilerstrasse 16, Amriswilerstrasse 11, Marktplatz 3)
- Neue Mieter: 27 Adressen, z.B. Migros, Müller und Neuroth, Salt, McOptic, Raiffeisen, Amplifon, Swica, Medbase. OSM ist dünn: Viele Läden tragen in OSM keine Adresse an diesen Strassen und fehlen deshalb.
- Register-Abgleich: 0 neue Treffer. Rathausstrasse 11 (UBS Sima) war schon erfasst. Heute sind UID und Sitz der Fondsleitung dazugekommen, übernommen von den übrigen Sima-Einträgen (Zefix-Stand 08.11.2026, heute nicht erneut abgefragt).
- Neue Eigentümer: 0
- Offen: **154** Adressen ohne Eigentümer. Alle haben jetzt eine Parzelle und ein E-GRID.
- Vermutungen nur in notes, `owner` bleibt leer: Marktplatz 1 UBS Sima (gleiche Parzelle 547 wie Rathausstrasse 11), Amriswilerstrasse 12 Migros Ostschweiz, Bahnhofstrasse 12 Raiffeisenbank Mittelthurgau, Rathausstrasse 22 Schulgemeinde oder Politische Gemeinde (Pestalozzi-Schulhaus, nicht als Mieter eingetragen).

## Anfragelisten
- `~/Downloads/Retail Map Anfragen/TG_Weinfelden.csv`: 140 Zeilen, nach E-GRID zusammengefasst. Prio 1/2/3 = 19/69/52. Spalten Link (ThurGIS, E/N amtlich, Muster abgeleitet und ungetestet) und Eigentuemer (leer).
- `TG_Weinfelden_Anleitung.txt`: ThurGIS-Einzelauskunft durch Kaito mit den Limits laut Nutzungsbestimmungen, dazu ein Mailentwurf an das Grundbuchamt und Notariat Weinfelden für Prio 2 und 3 (nicht versendet).
- Grundbuchamt verifiziert auf gni.tg.ch, Standortseite 1971: Lagerstrasse 8, +41 58 345 78 90, gnw@tg.ch (Mail als base64-mailto). Weinfelden namentlich aufgeführt. Nachgetragen in `tools/kantone_quellen.md`.

## Probleme
- `adressen.py` mischte die Bahnhofstrasse 1 aus Bussnang (2,2 km entfernt, gleicher Schlüssel) mit der Weinfelder Adresse. Position korrigiert, die Parzelle (492) kommt aus dem amtlichen Verzeichnis.
- Bahnhofstrasse 41 und 43 stehen in OSM, aber nicht im amtlichen Verzeichnis (die Suche nach 43 lieferte Gossau SG). Parzelle deshalb über die OSM-Position, die Lage in der Gemeinde Weinfelden ist geprüft (Parzellen 262 und 2851).
- Amriswilerstrasse 4 (OSM 980 m ausserhalb, amtlich nicht gefunden) wieder entfernt, der Eintrag stammte aus diesem Lauf.
- Keine Grundbuchportale abgefragt, keine Mails versendet.
