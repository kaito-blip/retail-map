# Tageslauf 08.11.2026: Winterthur (ZH)

## Strassen
Marktgasse, Untertor, Obertor, Steinberggasse, Stadthausstrasse. Das ist die bisherige Auswahl aus staedte.json, sie wurde bestätigt. `strassen_ok` steht jetzt auf true.

Ergebnis von `topstrassen.py` (Radius 900 m): Marktgasse 38 Läden, Stadthausstrasse 27, Steinberggasse 26, Untertor 23, Archplatz 20, Obergasse 18, Bahnhofplatz 13, Technikumstrasse 13, Wartstrasse 12, Obertor 13.
- Marktgasse und Untertor bilden die Hauptachse der Altstadt-Fussgängerzone vom Bahnhof bis zum Obertor.
- Steinberggasse und Obertor sind die Nebenachsen mit Fachgeschäften.
- Die Stadthausstrasse ist die parallele Achse mit Warenhäusern und Filialisten (C&A, Migros, IKEA-Planungsstudio).
- Nicht gewählt wurden Archplatz (Bahnhofsumfeld), Obergasse (Gastronomie), Technikumstrasse und Wartstrasse (Ausfallachsen).
- CITIES blieb unverändert. Dort stehen schon alle 5 Strassen sowie Bahnhofplatz, Casinostrasse, Graben, Oberer Graben, Metzggasse und Technikumstrasse.

## Zahlen
- **258 Adressen** aus OSM: Stadthausstrasse 70, Marktgasse 68, Steinberggasse 49, Obertor 36, Untertor 35. Davon haben 173 einen Mieter-POI.
- **Neue Mieter:** 161 Adressen. Die übrigen 12 Adressen mit Mieter hatten schon einen Eintrag.
- **Register-Abgleich:** 20 Winterthur-Adressen bestätigt, kein neuer Treffer.
  - Zum Register gehören AXA Fonds und AXA AST, SPSS IFC, Assetimmo, Swisscanto AST, UBS AST 1, UBS Swissreal und Direct Mixed Urban, Schroder ImmoPLUS sowie PSP.
  - Für die Stadt Winterthur gibt es weiterhin kein OGD-Liegenschaftsverzeichnis.
- **Neue Eigentümer: 0.** Für keine weitere Adresse gab es einen sicheren öffentlichen Beleg.
- **UID und Sitz aus Zefix:** für alle 20 Adressen mit Eigentümer ergänzt. Die UID der UBS Investment Foundation 1 (CHE-109.824.344, Bahnhofstrasse 45, Zürich) wurde neu abgefragt.
- **Hinweise in notes** («vermutlich …, ungeprüft», owner leer):
  - Obertor 16/22/26 und Stadthausstrasse 21/31 (Parzelle ST10053): vermutlich Stadt Winterthur. Die Stadt hat 2011 Obertor 16–26 und Stadthausstrasse 19/21 von der Fortuna Obertor AG übernommen (Abstimmungszeitung 13.02.2011). Der heutige Stand ist offen.
  - Stadthausstrasse 4a (Stadthaus), Marktgasse 20 (Rathaus) und Stadthausstrasse 57 (Rathausdurchgang, gleiche Parzelle ST7406): vermutlich Stadt Winterthur.
- **Parzelle und E-GRID** sind für alle 238 offenen Adressen gesetzt (Format «Winterthur ST…», E-GRID in notes). Die Daten stammen aus der Nachtlauf-CSV (geo.admin).
  - Stadthausstrasse 11 steht nicht im amtlichen Adressverzeichnis. Die Parzelle ST7793 wurde über die OSM-Koordinate bestimmt, in notes steht «prüfen».
- **Offen: 238 von 258 Adressen**, das sind 198 Parzellen.
- **SEED:** 5407 Einträge, 627 davon mit Eigentümer. Winterthur hat 258 Einträge, 20 davon mit Eigentümer. Gegen HEAD geprüft: kein bestehender Wert überschrieben, kein Key verloren.

## Anfrageliste
- `~/Downloads/Retail Map Anfragen/ZH_Winterthur.csv` hat 198 Parzellen, eine Zeile pro Parzelle.
  - Spalten: Prioritaet, Adressen, Parzelle, E-GRID, Mieter, Hinweis, Eigentuemer (leer).
  - Prio 1 = 73, Prio 2 = 87, Prio 3 = 38.
- `ZH_Winterthur_Anleitung.txt` beschreibt zwei Wege:
  - **Weg 1:** GIS-Browser ZH «Öffentliches Grundbuch», mit SMS und ca. 5 Abfragen pro Tag. Kaito fragt selbst einzeln ab.
  - **Weg 2:** Mailentwurf an das Notariat, Grundbuch- und Konkursamt Winterthur-Altstadt: Stadthausstrasse 12, 8400 Winterthur, 052 687 26 66, winterthur-altstadt@notariate-zh.ch.
  - Die Amtsadresse ist **verifiziert** (notariate-zh.ch, 08.11.2026). Das Amt ist für das Stadtquartier Winterthur-Stadt zuständig.
  - Nichts wurde versendet.
- Direktlinks: maps.zh.ch leitet auf geo.zh.ch/maps?initialMapIds=… um und verwirft dabei Koordinaten-Parameter. Ein Link pro Parzelle ist nicht dokumentiert, darum hat die CSV keine Link-Spalte.

## Probleme
- Swiss Prime Site hat laut immobilienbusiness.ch (28.01.2026, «Anlagestiftung kauft Geschäftshaus») ein Geschäftshaus am Untertor an die Profond Anlagestiftung verkauft.
  - Die Hausnummer wird im Artikel nicht genannt, deshalb wurde nichts eingetragen.
  - Kandidat für eine gezielte Abfrage.
- Untertor 30 (ZKB-Filiale, Parzelle ST7753): Im Stadtratsbeschluss zur Unterschutzstellung vom 30.06.2021 war die Grundeigentümerin nicht lesbar. Das PDF ist grösstenteils komprimiert.
- Die SPS-Medienmitteilung «Bedeutende Akquisition in Winterthur» (01.12.2017) ist unter der Cloudinary-URL nicht mehr abrufbar (404). Unter sps.swiss existiert eine englische Fassung, sie wurde nicht gelesen.
- Fremde untracked Dateien (tools/anfragen/, nachtlauf.sh, nachtauftrag_eigentuemer.md) wurden nicht committet.
