# Biel/Bienne (BE), Lauf 09.11.2026

## Strassen
Bisher in CITIES: Nidaugasse, Bahnhofstrasse, Zentralstrasse, Marktgasse, Dufourstrasse, Güterstrasse (bleiben drin).
Neu nach `topstrassen.py "Biel/Bienne" 15 900`: **Kanalgasse** (Parallele zur Nidaugasse, 8 Läden) und **Mühlebrücke** (Verbindung Nidaugasse zum Zentralplatz).
Neumarktstrasse, Neuengasse, Oberer Quai und Bahnhofplatz wurden nicht aufgenommen.

OSM führt Biel uneinheitlich: `Rue de Nidau / Nidaugasse`, `Rue de la Gare / Bahnhofstrasse`, daneben einsprachige Tags und Varianten mit Bindestrich. Die Karte vergleicht exakt, deshalb stehen die zweisprachigen Namen zusätzlich in CITIES. «Nidaugasse» und «Dufourstrasse» treffen in OSM nichts und bleiben nur als bestehende Einträge. Der amtliche Name der «Dufourstrasse» ist General-Dufour-Strasse / Rue du Général-Dufour.

Kernfilter: Zentralstrasse bis Nr. 72, General-Dufour-Strasse bis Nr. 35 (danach überwiegend Wohnen). Die Karte lädt die Strassen trotzdem ganz, die Aussennummern erscheinen dort ohne Daten.

`tools/adressen/biel_bienne.json` ist aus der Overpass-Fläche der Gemeinde Biel/Bienne (Relation 1682380) und dem GWR aufgebaut, nicht mit `adressen.py`.

## Zahlen
- Adressen: 275 (Zentralstrasse 63, Bahnhofstrasse 54, Nidaugasse 42, Kanalgasse 32, General-Dufour-Strasse 29, Marktgasse 21, Güterstrasse 19, Mühlebrücke 15).
- EXTRA: 42, davon 36 nur im GWR (u.a. Nidaugasse 5, 11, 15, 28, 34, 44, 46, 49, 54, 64, 66, 68, 74) und 6 seltene OSM-Schreibweisen unter dem zweisprachigen Namen. Ohne Nebenbauten und Garagen.
- SEED: 298 Einträge für Biel/Bienne. Das sind mehr als Adressen, weil 23 Adressen in OSM unter zwei Schreibweisen vorkommen und beide Keys dieselben Daten tragen, dazu Register-Einträge ausserhalb des Kerns.
- Mieter: 156 Adressen mit Mieter, 153 davon neu. Bei 90 Läden ohne Hausnummer per Gebäudeumriss zugeordnet, wenn das Gebäude genau eine Adresse hat.
- Neue Eigentümer: 11 Adressen. Register: Nidaugasse 14 und 42 (AXA Anlagestiftung), Nidaugasse 15 (AXA Real Estate Fund), Nidaugasse 40 (Pensimo Proreal), Mühlebrücke 2 (UBS Anlagestiftung 1), General-Dufour-Strasse 18, 26, 29a sowie Mühlebrücke 5, 5a (Einwohnergemeinde). Von Hand: General-Dufour-Strasse 17 (AXA Anlagestiftung, im Register als «Dufourstr. 17»).
- Eigentümer total: 21 von 275 Adressen. UID und Sitz bei allen Firmen ergänzt, Procimmo SICAV neu aus Zefix (CHE-446.577.045).
- Parzelle und E-GRID: für alle 254 offenen Adressen.
- Offen: 254 Adressen auf 213 Parzellen.

## Anfragelisten
- `~/Downloads/Retail Map Anfragen/BE_Biel_Bienne.csv`: 213 Parzellen, Prio 1: 75, Prio 2: 87, Prio 3: 51.
- `~/Downloads/Retail Map Anfragen/BE_Biel_Bienne_Anleitung.txt`: GRUDIS public (AGOV, Kaito fragt einzeln ab, keine Direktlinks) und Mailentwurf an das Grundbuchamt Seeland, Schloss, Hauptstrasse 6, 2560 Nidau, +41 31 635 25 50, gba.sl@be.ch. Kontakt **verifiziert** am 09.11.2026 auf gba.dij.be.ch. Zuständigkeit für Biel nur abgeleitet (Verwaltungsregion Seeland), keine Gemeindeliste gefunden. Nichts versendet.

## Probleme und offene Punkte
- Keine Antworten in `Retail Map Anfragen/Antworten/` vorhanden.
- Nur als Hinweis in notes, `owner` leer: Nidaugasse 5 (vermutlich Geschäftshaus Nidaugasse Nr.5 A.G., CHE-101.296.571, Zweck laut Zefix Halten und Verwalten dieses Hauses), Nidaugasse 35 (Vermietung über Coop Immobilien AG, Eigentum nicht belegt).
- Vier offene Adressen liegen auf der Parzelle eines bekannten Eigentümers (Bahnhofstrasse 13, General-Dufour-Strasse 1, 22, 24). Nur als «vermutlich» vermerkt, weil Baurecht oder abweichende Eigentümer möglich sind.
- Bahnhofstrasse 20, 22 und 42a: amtliche Vermessung und GWR nennen verschiedene Parzellen (AV gilt, in der Liste markiert).
- Nidaugasse 31 und Kanalgasse 23 stehen nur in OSM, nicht im GWR.
- General-Dufour-Strasse 17 wurde mit «Dufourstr. 17» gleichgesetzt. Eine zweite Dufour-Strasse gibt es in Biel nicht, im Dokument steht aber nur die Kurzform.
- 54 Läden in Gebäuden mit mehreren Adressen sind nicht als Mieter eingetragen, sondern in notes und Spalte Hinweis (u.a. Coop City, Migros, Loeb, PKZ). 105 Läden ohne Hausnummer lagen in keinem OSM-Gebäude und wurden nicht zugeordnet.
- Die Gebäude-Zuordnung beruht auf OSM, einzelne Mieter können veraltet sein.
- Websuche zu Manor, Loeb und Coop City lieferte keinen belegten Eigentümer.
