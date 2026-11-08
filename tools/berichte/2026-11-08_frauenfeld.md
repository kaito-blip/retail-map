# Frauenfeld (TG), Lauf 08.11.2026

## Strassen
Bisher in CITIES: Zürcherstrasse, Rheinstrasse, Freiestrasse, Bankplatz, Promenadenstrasse. Diese bleiben drin.
Neu ergänzt: **Freie-Strasse** (so lautet der OSM-Name, «Freiestrasse» trifft in OSM keine Adresse), **Bahnhofstrasse**, **Bahnhofplatz**, **Rathausplatz**.
Die Wahl folgt topstrassen.py (Zürcherstrasse 11 Läden, Bahnhofplatz 11, Bahnhofstrasse 7, Grabenstrasse 4, Rathausplatz 2). Die Grabenstrasse ist nicht aufgenommen, weil sie vor allem Wohnstrasse am Altstadtring ist.
Die Zürcherstrasse ist rund 4 km lang (264 Adressen). Für die Liste ist sie deshalb auf 450 m um die Altstadt beschränkt (etwa Nr. 134 bis 245), die Bahnhofstrasse auf 600 m (etwa Nr. 43 bis 103).
staedte.json: `strassen_ok` true.

## Zahlen
- Adressen: 222 (Zürcherstrasse 97, Bahnhofstrasse 36, Freie-Strasse 27, Rheinstrasse 22, Bahnhofplatz 15, Promenadenstrasse 14, Rathausplatz 7, Bankplatz 4)
- Neue Mieter: 42 Adressen (insgesamt 46 mit Mieter), z.B. Manor/Coop Vitality/Christ (Zürcherstrasse 138), PKZ, Fielmann, Beldona, Orell Füssli, Migros/C&A/Interdiscount (Bahnhofplatz/Bahnhofstrasse 70-72), Micasa, JYSK, UBS, Raiffeisen, TKB
- Register-Abgleich: 0 neue Eigentümer. Die 10 Treffer an diesen Strassen waren schon eingetragen (AXA AST Bahnhofplatz 65 bis 71, SBB Bahnhofplatz 75, Novavest Zürcherstrasse 212/237/237a/239, assetimmo Zürcherstrasse 229).
- UID und Sitz aus Zefix bei 12 Einträgen ergänzt: Novavest CHE-287.294.566 (Zürich), Fundamenta CHE-113.353.632 (Zug), AXA AST, SBB, assetimmo. Für Helvetica Property Investors AG gab es in Zefix keinen Treffer, die Felder bleiben leer.
- Neue Eigentümer: 0
- Offen: **212** Adressen ohne Eigentümer. Alle haben jetzt eine Parzelle und ein E-GRID.
- Vermutungen nur in notes, owner bleibt leer: Bahnhofstrasse 75 SBB, Bahnhofplatz 73 AXA AST, Zürcherstrasse 227 assetimmo und Bahnhofstrasse 92 Novavest (jeweils gleiche Parzelle wie ein Register-Eintrag); Migros (70-72), Kanton TG (Promenadenstrasse 8/12/12a), Stadt (Bankplatz 3), Evangelische Kirchgemeinde (Freie-Strasse 12).

## Anfragelisten
- `~/Downloads/Retail Map Anfragen/TG_Frauenfeld.csv`: 168 Zeilen, nach E-GRID zusammengefasst, Prio 1/2/3 = 31/95/42, Spalten Link (ThurGIS) und Eigentuemer leer.
- `TG_Frauenfeld_Anleitung.txt`: ThurGIS-Einzelauskunft durch Kaito, Limits laut Nutzungsbestimmungen, Mailentwurf an das Grundbuchamt für Prio 2 und 3 (nicht versendet).
- Grundbuchamt und Notariat Frauenfeld, Langfeldstrasse 53a, 8510 Frauenfeld, 058 345 77 77, gnf@tg.ch. Verifiziert auf gni.tg.ch (Standortseite, mailto-Link). In kantone_quellen.md nachgetragen.

## Probleme / Hinweise
- 8 Adressen findet die amtliche Suche nicht (Nummernbereiche «70-72», «145;147», Bahnhofstrasse 70/75/78/79/80). Ihre Parzelle wurde über die OSM-Koordinate bestimmt und in notes vermerkt.
- Der ThurGIS-Direktlink (E/N/zoom) ist aus den Standardparametern des mf-geoadmin3-Viewers abgeleitet und nicht geöffnet. Ersatzweise das E-GRID ins Suchfeld kopieren.
- Die ThurGIS-Limits sind nicht beziffert, nur «pro Stunde, Tag und Woche limitiert».
- Kein Grundbuch- oder Eigentümerportal wurde abgefragt. Keine Antworten in `Antworten/` für TG.
- Ein Privacy-Hook hat Bash-Befehle mit der Absender-Mail blockiert. Die Anleitung wurde deshalb mit dem Write-Tool geschrieben.
