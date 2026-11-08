# Pfäffikon SZ, Lauf 08.11.2026

## Strassen
- Bisher in CITIES: Bahnhofstrasse, Churerstrasse, Schindellegistrasse, Eichenstrasse (bleiben).
- Neu: **Gwattstrasse** (Seedamm-Center mit Migros, Coop, Manor-Umfeld, H&M, C&A, PKZ, Orell Füssli usw.). Laut topstrassen.py (Radius 1500 m) die mit Abstand stärkste Strasse (14 Läden).
- Seedammstrasse aus dem staedte.json-Vorschlag nicht übernommen (0 Läden).
- **CITIES-Fix:** `q` war «Pfäffikon, Freienbach». Dafür liefert Nominatim nur einen Node, die Karte lud also keine Adressen. Neu ist `q` **«Freienbach»** (Relation 1683073). Innerhalb der Gemeinde gibt es die fünf Strassen nur in Pfäffikon (alle PLZ 8808/8807, keine Doppelungen).
- staedte.json: `ort` neu «Pfäffikon SZ@47.2003055,8.7780752» (sonst Verwechslung mit Pfäffikon ZH), `radius` 1500.

## Zahlen
- Adressen: 167 (Churerstrasse 98, Schindellegistrasse 38, Gwattstrasse 11, Bahnhofstrasse 10, Eichenstrasse 10)
- Neue Mieter: 27 Adressen. Nicht übernommen als Mieter: Feuerwehr, Schulhaus, Kindergarten, Polizeiposten, Tesla Supercharger. «Seedamm-Center» steht in notes.
- Neue Eigentümer: 2 (Churerstrasse 120 und 122: UBS (CH) Property Fund Direct 1a Immo PK, Baurecht, UID CHE-102.674.664)
- Parzellen: alle 167 (Grundbuchkreis Freienbach, E-GRID in notes)
- Offen: 165 Adressen ohne Eigentümer (124 Grundstücke)
- Vermutlich, ungeprüft (nur notes): Seedamm-Center, Gwattstrasse 11/13/15/17 = eine Parzelle Freienbach 2115 → Seedamm-Immobilien AG, Freienbach (CHE-102.431.363, Zweck laut Zefix: Halten und Verwaltung der Seedamm-Center-Liegenschaft)

## Anfragelisten
- ~/Downloads/Retail Map Anfragen/SZ_Pfäffikon_SZ.csv (124 Zeilen, Priorität 1: 10, 2: 63, 3: 51; Kartenlink je Grundstück, Spalte Eigentuemer leer)
- ~/Downloads/Retail Map Anfragen/SZ_Pfäffikon_SZ_Anleitung.txt: WebGIS SZ (Captcha je Abfrage, Kaito fragt selbst ab) und Mailentwurf an das **Notariat und Grundbuchamt Höfe**, Rebhaldenstrasse 15, 8807 Freienbach, info@notariat-hoefe.ch (verifiziert 08.11.2026 über hoefe.ch → notariat-hoefe.ch). Nichts versendet.
- Antworten von Kaito lagen keine vor.

## Probleme
- **Fehler im Register-Abgleich behoben:** `register_abgleich.py` hat «Pfäffikon ZH» über den Alias «pfaffikon» auf Pfäffikon SZ gelegt. Dadurch standen SBB-Einträge auf Bahnhofstrasse 11 und 13 (SBB-Parzelle 13178 liegt in Pfäffikon ZH). Diese Einträge stammten aus diesem Lauf und sind zurückgenommen (Erklärung in notes). Neu filtert der Abgleich Treffer, deren Kantonszusatz im Ortsnamen («ZH», «BE», «(SG)») nicht zum Kanton der Stadt passt. Die Spalte `kanton` zählt bewusst nicht, weil sie in Registern teils falsch ist (Davos «VS», UBS 1a «Pfäffikon ZH» für Churerstrasse 120/122, die amtlich nur in Pfäffikon SZ existiert).
- **Altfehler gefunden, nicht gelöscht:** brugg|bahnhofstrasse|8 trägt seit einem früheren Lauf SBB als Eigentümer, aus der Register-Zeile «Bahnhofstrasse 8, 2555 Brügg BE». Der Eintrag ist nur mit einer Warnnotiz versehen und muss von Hand geprüft und gegebenenfalls geleert werden.
- parzelle.py prüft die PLZ nicht: «Churerstrasse 148» traf Buchs SG. Für diese Adresse korrigiert über die OSM-Position. Fünf Adressen gibt es amtlich nicht (Bahnhofstrasse 2 und 28, Churerstrasse 55 und 148, Schindellegistrasse 8), ihre Parzelle stammt aus der OSM-Position. Bei vier Mehrfachnummern (z.B. Schindellegistrasse 61a,61b,61c) wurde die erste Nummer verwendet.
- OSM ist im Zentrum dünn (Bahnhofstrasse und Churerstrasse mit wenigen POIs). Mieterliste daher unvollständig.
