# Einsiedeln (SZ), Lauf 09.11.2026

## Strassen
Die fünf Strassen in CITIES bleiben: **Hauptstrasse, Klosterplatz, Kronenstrasse, Schmiedenstrasse, Bahnhofplatz**. Neu dazu kommt die **Eisenbahnstrasse** (10 Läden laut topstrassen.py, Achse vom Bahnhof ins Zentrum).
`q` «Einsiedeln» liefert die Gemeinde-Relation 1683065, also korrekt. `strassen_ok` steht jetzt auf true.
Nicht aufgenommen: Zürichstrasse (Ausfallachse mit Garagen und Fachmärkten bis 1,3 km) und Schwanenstrasse (parallele Nebenstrasse, 9 Läden auf 34 Adressen). Die Schwanenstrasse wäre ein Kandidat für eine siebte Strasse.

## Zahlen
- **Adressen:** 190 (Hauptstrasse 83, Kronenstrasse 32, Schmiedenstrasse 32, Eisenbahnstrasse 27, Bahnhofplatz 12, Klosterplatz 4)
- **Davon aus OSM:** 148. **Aus dem GWR ergänzt (EXTRA):** 42, darunter der ganze Klosterplatz, der in OSM keine Hausnummern hat.
- **Neue Mieter:** 85 Adressen. 13 Mieter-POIs ohne Adress-Tag wurden auf 12 Adressen per Lage zugeordnet (unter 8 m, bei Broggi's bis 17 m), das steht in notes.
- **Register-Abgleich:** 1 neuer Eigentümer, Hauptstrasse 73 (Register «73 – 79», Parzelle 248, VERIT für Raiffeisen Futura Immo Fonds). Hauptstrasse 75, 77 und 79 waren schon eingetragen.
- **UID und Sitz aus Zefix:** für alle vier ergänzt, CHE-102.499.361, Klausstrasse 48, 8008 Zürich.
- **Neue Eigentümer:** 1
- **Offen:** **186** Adressen ohne Eigentümer. Alle haben Parzelle und E-GRID (152 Grundstücke).
- **Vermutungen** stehen nur in notes, owner bleibt leer:
  - Klosterplatz 1.11, 1.58, 2 (Parzelle 73): Kloster Einsiedeln
  - Hauptstrasse 78 (Rathaus): Bezirk Einsiedeln
  - Eisenbahnstrasse 20 (Bezirksamt, Bezirksgericht): öffentliche Hand
  - Bahnhofplatz 1 (Bahnhofsgebäude): Bahnunternehmen

## Anfragelisten
- `~/Downloads/Retail Map Anfragen/SZ_Einsiedeln.csv`
  - 152 Zeilen, nach E-GRID zusammengefasst
  - Priorität 1/2/3: 30/58/64
  - Spalte Link (Kartenlink mit Fadenkreuz, Muster abgeleitet und ungetestet), Spalte Eigentuemer leer
- `SZ_Einsiedeln_Anleitung.txt`
  - Kaito fragt im WebGIS SZ einzeln ab (Captcha pro Abfrage, kein Stockwerkeigentum)
  - Mailentwurf an das Grundbuchamt, nicht versendet
- **Notariat Grundbuch- und Konkursamt Einsiedeln:** Schwanenstrasse 4, Postfach 346, 8840 Einsiedeln, 055 418 30 30, info@notariat-einsiedeln.ch
  - Verifiziert auf notariat-einsiedeln.ch und in der Adressliste notare-schwyz.ch
  - In kantone_quellen.md nachgetragen

## Probleme / Hinweise
- **10 OSM-Adressen fehlen amtlich:** Hauptstrasse 1, 2a, 13, 22, 34, 37, 75, 77 und Schmiedenstrasse 6, 25. Ihre Parzelle kommt aus der OSM-Koordinate, das steht in notes. Hauptstrasse 75 und 77 sind ausser in OSM auch im Fondsregister geführt.
- **Hauptstrasse 1** fällt per Position auf die Bahnhofsparzelle 5640 und ist in der Liste mit Bahnhofplatz 1 und 7 zusammengefasst. Vor einer Abfrage prüfen, ob die Adresse real existiert.
- **Hauptstrasse 83:** OSM nennt noch Credit Suisse, heute UBS, Filiale ungeprüft.
- **Klosterplatz:** Von den amtlichen Unternummern 1.xx sind nur Arkade (1.11) und Klosterladen (1.58) erfasst, die übrigen sind Klosterbetriebe ohne Ladennutzung.
- **Register-Abgleich:** Der erste Abgleich traf Hauptstrasse 73 nicht, weil die Adresse noch nicht im SEED stand. Deshalb nach dem Setzen der Adressen ein zweites Mal gelaufen.
- **Kein Portal abgefragt:** Kein Grundbuch- oder Eigentümerportal wurde abgefragt. Den Ordner `Antworten/` gibt es nicht, also lagen keine Antworten vor.
