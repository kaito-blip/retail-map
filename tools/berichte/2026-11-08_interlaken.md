# Interlaken (BE), Lauf 2026-11-08

## Strassen
Höheweg, Bahnhofstrasse, Marktgasse, Postgasse, Jungfraustrasse, Rosenstrasse, Centralstrasse, Aarmühlestrasse. Alle stammen aus CITIES und bleiben drin, nichts neu in CITIES. Bahnhofplatz steht ebenfalls in CITIES, hat aber weder in OSM noch im amtlichen Verzeichnis Adressen und ist deshalb nicht in staedte.json. `q: 'Interlaken'` (Relation 1682493). topstrassen.py liefert in Interlaken wenig (OSM-Läden meist ohne Adresse), massgebend war die Begehung vom 21.09.2026.

## Zahlen
- Adressen: 439 (Höheweg 115, Jungfraustrasse 82, Bahnhofstrasse 50, Marktgasse 47, Postgasse 45, Centralstrasse 41, Rosenstrasse 31, Aarmühlestrasse 28)
- Neue Mieter: 105 Adressen mit 147 Mietern aus OSM, davon ein grosser Teil über Gebäudezuordnung von Läden ohne eigene Adresse. Nichts überschrieben. Bestehende Begehungsdaten blieben. Insgesamt 161 Adressen mit Mieter.
- Neue Eigentümer: 0. Register-Abgleich: nur Höheweg 74a (Kanton Bern) bestätigt.
- Eigentümer bekannt: 5 (GRUDIS public 25.09.2026: Höheweg 16, Bahnhofstrasse 3, 8, 25a; Register: Höheweg 74a)
- Parzellen: alle 434 offenen Adressen mit Parzelle («Interlaken <Nr>») und E-GRID in notes, 311 Parzellen
- Offen (ohne Eigentümer): 434

## Anfrageliste
- `~/Downloads/Retail Map Anfragen/BE_Interlaken.csv`: 311 Parzellen, Priorität 1: 76, 2: 99, 3: 136. Spalte Eigentuemer leer, Link nur zum Katasterplan auf map.geo.admin, weil GRUDIS public keine Direktlinks hat. Die ältere Nachtlauf-Datei `Parzellen/BE_Interlaken.csv` bleibt unverändert.
- `BE_Interlaken_Anleitung.txt`: Weg A GRUDIS public (AGOV, Kaito fragt einzeln ab, etwa 10 bis 20 pro Tag, kein Limit publiziert), Weg B Mailentwurf an das Grundbuchamt Oberland, Allmendstrasse 18, 3600 Thun, gba.ol@be.ch. Verifiziert auf gba.dij.be.ch am 08.11.2026 (Seiten Oberland und Dienststelle Interlaken). Nichts versendet.

## Vermutungen in notes (owner leer)
- Höheweg 41: vermutlich Swiss Hotel Properties AG oder andere Gesellschaft der Aevis-Victoria-Gruppe, ungeprüft. Die öffentlichen Quellen nennen die Parzelle nicht und widersprechen sich teils.
- Bahnhofstrasse 28: vermutlich BLS AG (Bahnhof Interlaken West), ungeprüft.
- Marktgasse 17: vermutlich Raiffeisenbank Jungfrau, ungeprüft.
- Bahnhofstrasse 25f: gleiche Parzelle 1359 wie 25a (Hodel), Eigentum dort noch zu bestätigen.

## Probleme / Hinweise
- adressen.py holt im 2500-m-Radius auch die Bahnhofstrasse von Unterseen (gleiche Hausnummern, Datensätze vermischt). tools/adressen/interlaken.json wurde deshalb aus der Gemeindefläche (Overpass-Area) neu aufgebaut. 7 Adressen nur in Unterseen entfallen.
- Acht Adressen sind amtlich nicht verzeichnet, Parzelle über OSM-Position: Höheweg 19a, 75a, 92-94, 121, 123a, Jungfraustrasse 13, 46, Marktgasse 61.
- Die Nachtlauf-CSV `Parzellen/BE_Interlaken.csv` ist bei Höheweg 19a falsch: Parzelle 740 gehört zu Höheweg 19a in Oberdiessbach. Hier gilt 697 über die OSM-Position.
- Offensichtlicher OSM-Müll wurde nicht übernommen («EG», «Bar & Restaurant»), Tippfehler und Dubletten bereinigt.
- Jungfraustrasse 1: Die bestehende Notiz bei Höheweg 16 nennt sie als Teil von Parzelle 384, der amtliche Adresspunkt liegt aber auf Parzelle 381. In notes und CSV markiert.
- Bahnhofstrasse 3 hat den ownerType «Privatpersonen (einfache Gesellschaft)», keinen gültigen Auswahlwert. Bestehender Wert, nicht geändert.
- Quellen zu Höheweg 37 (Metropole) ohne Eigentümerangabe.
- Keine Portalabfragen, keine Mails, keine Formulare.
