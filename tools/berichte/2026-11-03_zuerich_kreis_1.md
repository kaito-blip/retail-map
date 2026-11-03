# Tageslauf 03.11.2026: Zürich (Kreis 1)

## Strassen
Bahnhofstrasse, Rennweg, Löwenstrasse, Limmatquai, Niederdorfstrasse.
Grundlage: `topstrassen.py` (Bahnhofstrasse 81 Läden, Löwenstrasse 43, Limmatquai 31, Rennweg 24, Niederdorfstrasse 11). Langstrasse, Badenerstrasse, Lagerstrasse und Josefstrasse ausgelassen, weil sie ausserhalb von Kreis 1 liegen; Bleicherweg steht schon im Preset «Zürich (übrige Kreise)». Alle fünf Strassen waren bereits in CITIES, deshalb keine Änderung an CITIES.

## Zahlen
- Adressen an den fünf Strassen (OSM): 323 (Bahnhofstrasse 91, Limmatquai 71, Niederdorfstrasse 59, Löwenstrasse 53, Rennweg 49)
- Neue Mieter (tenant): 163 Adressen, alle als neue SEED-Einträge. Bestehende Mieter blieben unverändert. Herausgefiltert wurden 25 OSM-POIs ohne Ladenbezug (Büros/AG/GmbH, Arztpraxen, Polizeiposten, Konsulat, Synagoge, Notariat, Bibliothek).
- Parzelle und E-GRID (geo.admin): 269 Adressen eingetragen (`parcel` «Zürich AAxxxx», E-GRID in notes). Kein Treffer bei Bahnhofstrasse 15, Limmatquai 140, Löwenstrasse 50a und Rennweg 44; diese Adressen gibt es im amtlichen Adressregister nicht.
- Neue Eigentümer: 1. **Bahnhofstrasse 42**: Swiss Prime Site (Alleineigentum), Quelle Finanzbericht 2025, Liegenschaftsverzeichnis. Juristische Eigentümerin im Grundbuch vermutlich Swiss Prime Site Immobilien AG, ungeprüft.
- Nur in notes, weil ungeprüft: **Bahnhofstrasse 32 (Leuenhof)**, vermutlich Swiss Prime Anlagestiftung (Kauf 2016 laut finews.ch).
- Offen (ohne Eigentümer) an den Top-Strassen: **272 von 323**. Bahnhofstrasse 54 bis 110 ist aus früheren Läufen weitgehend erfasst.
- SEED: 371 → 639 Einträge, 117 mit Eigentümer (Zürich Kreis 1: 330 Einträge, 59 mit Eigentümer). Abgleich mit dem Stand vor dem Lauf: kein bestehender Wert verändert oder gelöscht.

## Anfragelisten
- `~/Downloads/Retail Map Anfragen/ZH_Zürich (Kreis 1).csv` mit 272 Zeilen (Adresse;Parzelle;E-GRID;Mieter)
- `~/Downloads/Retail Map Anfragen/ZH_Zürich (Kreis 1)_Anleitung.txt`
  - Weg 1: GIS-Browser ZH «Öffentliches Grundbuch», Einzelabfrage mit SMS, etwa 5 pro Tag. Das reicht für 272 Adressen nicht in vernünftiger Zeit.
  - Weg 2: Mail-Entwurf ans Notariat, Grundbuch- und Konkursamt Zürich (Altstadt), Löwenstrasse 11, Postfach, 8022 Zürich, 044 752 36 00, zuerich-altstadt@notariate-zh.ch. Am 03.11.2026 auf notariate-zh.ch verifiziert. Nicht verifiziert ist, ob das Amt auch für Limmatquai und Niederdorfstrasse zuständig ist. Die Mail wurde nicht versendet.

## Probleme
- Overpass: `zentrum("Zürich")` (CH-weite Area-Abfrage) lieferte bei overpass.osm.ch eine Fehlerseite statt JSON. Danach meldete der Server «duplicate_query», und der Fallback overpass-api.de scheitert am SSL-Handshake (LibreSSL 2.8.3 im System-Python). Gelöst, indem das Zentrum manuell übergeben wurde (`"Zürich@47.3744489,8.5410422"`), nach 2,5 Minuten Pause.
- `adressen.py` macht aus «Zürich (Kreis 1)» den Dateinamen `z_rich_kreis_1_.json`, weil die Regex keine Umlaute kennt. Das funktioniert, sieht aber unschön aus.
- PSP Swiss Property: Den Geschäftsbericht 2025 mit Liegenschaftsverzeichnis habe ich nicht als PDF gefunden (psp.info liefert 404). Ein nächster Lauf könnte ihn nach weiteren Eigentümern an der Bahnhofstrasse und Löwenstrasse durchsuchen.
- Keine Grundbuchportale abgefragt, nichts versendet.
