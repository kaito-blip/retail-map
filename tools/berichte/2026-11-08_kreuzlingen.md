# Kreuzlingen (TG), Lauf 08.11.2026

## Strassen
In CITIES standen schon: Hauptstrasse, Bahnhofstrasse, Konstanzerstrasse, Bärenplatz, Sonnenstrasse. Sie bleiben alle drin, nichts ergänzt.
Laut topstrassen.py (Radius 800) haben nur die Hauptstrasse (8 Läden) und die Sonnenstrasse (7, davon 8 POI allein bei Nr. 16 mit Manor) nennenswert Läden. Alle anderen Strassen haben höchstens 2. Ein besserer Kandidat zum Ergänzen fehlt.
- Bärenplatz: Weder OSM noch das amtliche Adressverzeichnis führen dort Adressen. Die Häuser am Platz laufen unter Hauptstrasse. Der Eintrag bleibt trotzdem stehen.
- Hauptstrasse und Konstanzerstrasse haben weit entfernte Aussensegmente (Hauptstrasse 117 bis 147 ungerade, 122 und 128a bis 146, Konstanzerstrasse 113 bis 125, je rund 2 km vom Zentrum). Die Adressdatei ist deshalb auf 1500 m gefiltert (29 Adressen raus).
staedte.json: `strassen_ok` true.

## Zahlen
- Adressen: 267 (Hauptstrasse 120, Konstanzerstrasse 78, Sonnenstrasse 43, Bahnhofstrasse 26)
- Neue Mieter: 34 Adressen, z.B. Manor, Coop Vitality, Christ, Visilab, Interdiscount (Sonnenstrasse 16), Migros (Hauptstrasse 63), Sunrise/Neuroth, UBS, TKB, Raiffeisen, Migros Bank, Swisscom, Davids Mode
- Register-Abgleich: 0 neue Treffer. SBB Bahnhofstrasse 12 war schon erfasst. Heute sind UID CHE-102.909.703 und der Sitz aus Zefix dazugekommen (gleiche Werte wie bei den übrigen SBB-Einträgen). Die anderen Kreuzlinger Registerzeilen (AXA, Pensimo, PKBS, UBS, Swisscanto, Mobimo u.a.) liegen alle nicht an diesen Strassen.
- Neue Eigentümer: 0
- Offen: **266** Adressen ohne Eigentümer. Alle haben jetzt eine Parzelle und ein E-GRID (262 aus der Parzellen-Datei vom Nachtlauf, 4 über die OSM-Koordinate: Bahnhofstrasse 7, Bahnhofstrasse 14, Hauptstrasse 106, Konstanzerstrasse 15-15a).
- Vermutungen nur in notes, `owner` bleibt leer: Bahnhofstrasse 14 SBB (gleiche Parzelle 1717 wie Nr. 12), Hauptstrasse 63 Migros Ostschweiz, 62 Stadt Kreuzlingen, 87/89 Kanton TG (ehemaliges Kloster, heute PMS), 85 Kath. Kirchgemeinde (St. Ulrich), 39 TKB, Konstanzerstrasse 13 Kanton TG (Bezirksgericht).

## Anfragelisten
- `~/Downloads/Retail Map Anfragen/TG_Kreuzlingen.csv`: 193 Zeilen, nach E-GRID zusammengefasst. Prio 1/2/3 = 17/82/94. Die vermutlich öffentlichen Eigentümer stehen in Prio 3. Spalten Link (ThurGIS, E/N aus der OSM-Position umgerechnet) und Eigentuemer (leer).
- `TG_Kreuzlingen_Anleitung.txt`: ThurGIS-Einzelauskunft durch Kaito mit den Limits laut Nutzungsbestimmungen, dazu ein Mailentwurf an das Grundbuchamt Kreuzlingen für Prio 2 und 3 (nicht versendet).
- Grundbuchamt Kreuzlingen, Bachstrasse 11, 8280 Kreuzlingen, 058 345 78 30, gnk@tg.ch. Verifiziert auf gni.tg.ch/standorte/kreuzlingen/grundbuchamt-kreuzlingen.html/1968. In kantone_quellen.md nachgetragen.

## Probleme / Hinweise
- Der ThurGIS-Direktlink ist wie bei Frauenfeld abgeleitet und nicht geöffnet.
- Die ThurGIS-Limits sind nicht beziffert. Das Kontingent teilt sich mit der Frauenfeld-Liste.
- Kein Grundbuch- oder Eigentümerportal wurde abgefragt. In `Antworten/` liegen keine Antworten für TG.
- In der Liste der Ladenstrassen ist Kreuzlingen dünn. Ein Teil des Handels liegt in Einkaufszentren und an Ausfallachsen (z.B. Migros Hauptstrasse 117 im Aussensegment) und ist hier bewusst nicht erfasst.
