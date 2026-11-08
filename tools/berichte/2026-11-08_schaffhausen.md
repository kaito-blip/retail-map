# Tageslauf 08.11.2026: Schaffhausen (SH)

## Strassen
In CITIES standen schon Vordergasse, Fronwagplatz, Vorstadt, Schwertstrasse, Oberstadt, Webergasse und Kirchhofplatz. Sie bleiben alle drin, index.html/CITIES wurde nicht geändert. `strassen_ok` steht jetzt auf true.

`topstrassen.py "Schaffhausen" 10 800`: Vordergasse 27 Läden, Vorstadt 15, Fronwagplatz 13, Webergasse 8, Bahnhofstrasse 4, Unterstadt 3, Stadthausgasse 6, Neustadt 5, Schwertstrasse 4, Oberstadt 5.

Gewählt (staedte.json):
- **Vordergasse**: Hauptachse der Fussgängerzone, Filiallage.
- **Fronwagplatz**: zentraler Platz mit Manor, Fielmann, Lush, Sunrise.
- **Vorstadt**: nördliche Fussgängerzone Richtung Schwabentor, Filiallage.
- **Webergasse**: Altstadtgasse mit vielen kleinen Läden.
- **Schwertstrasse** und **Oberstadt**: kurze Verbindungen am Fronwagplatz und zum Obertor, beide schon in CITIES. Sie wurden mitgenommen, weil fast jedes Haus dort ein Ladenlokal hat.
- Nicht gewählt: Bahnhofstrasse (Verkehrsachse), Unterstadt, Stadthausgasse, Neustadt (Nebenlagen). Kirchhofplatz bleibt in CITIES, wurde aber nicht bearbeitet.

## Zahlen
- **226 Adressen** aus OSM (Vordergasse 67, Vorstadt 58, Webergasse 48, Fronwagplatz 23, Oberstadt 22, Schwertstrasse 8). 221 davon sind neu im SEED, 5 standen schon dort.
- **Abgleich mit dem amtlichen Gebäudeadressverzeichnis:** Es fehlen in OSM nur Unternummern (Fronwagplatz 5.1, 5.2, 7.11, Oberstadt 21.1, Schwertstrasse 9.1, Vordergasse 37.1, Vorstadt 55.11, Webergasse 28.1). Das sind Nebengebäude, deshalb kein EXTRA. Nur in OSM stehen Vorstadt «22;24», «30-32» (Parzelle über die erste Nummer) und Vorstadt 6 (Parzelle über den OSM-Punkt, gleiche Parzelle wie Nr. 8, Hinweis in notes).
- **Neue Mieter:** 85 Adressen aus OSM-POIs, z.B. Manor · Coop (Fronwagplatz 1), Fielmann, Lush, Sunrise, Interdiscount (Vorstadt 33), Amavita (Vorstadt 30-32), Migros Bank.
- **Register-Abgleich** (`register_abgleich.py --schreiben`): **0 neue Treffer**. Die 5 bekannten Eigentümer sind bestätigt: Vordergasse 3 = AXA Anlagestiftung, Vorstadt 33 und Schwertstrasse 6 = UBS Interswiss, Vorstadt 67/69 = UBS Anlagestiftung 4. Die übrigen Schaffhauser Registerzeilen (SBB Bahnhofstrasse, Novavest Bahnhofstrasse 46, Wohnbauten) liegen ausserhalb der gewählten Strassen. Es gab keinen Konflikt in Schaffhausen.
- **Neue Eigentümer: 0.** Keine sichere öffentliche Quelle gefunden, und es wurde nichts geraten.
- **UID/Sitz ergänzt** für die 5 bekannten Eigentümer: UBS Fund Management (Switzerland) AG CHE-102.674.664, AXA Anlagestiftung CHE-380.550.119 (beide aus bestehenden SEED-Einträgen anderer Städte), UBS Investment Foundation 4 CHE-109.418.754, c/o UBS AG, Bahnhofstrasse 45, 8001 Zürich (Zefix REST, 08.11.2026).
- **Parzelle und E-GRID** für alle 221 offenen Adressen gesetzt («Schaffhausen <Nr>», E-GRID in notes). 220 kamen über die amtliche Adresse, 1 über den OSM-Punkt. Mehrfach belegte Parzellen (z.B. 28 = Vorstadt 53 bis 63, 331 = Vorstadt 35 bis 41, 110 = Vorstadt 30/32 und Webergasse 49) sind plausible Blockrandbauten, keine Strassenparzellen.
- **Offen: 221 von 226.**
- **SEED:** 3657 Einträge, 625 mit Eigentümer. Gegen den Stand vor dem Lauf geprüft: kein bestehender Wert überschrieben, kein Eintrag verloren. Die JS-Syntax ist geprüft.

## Anfrageliste
- `~/Downloads/Retail Map Anfragen/SH_Schaffhausen.csv`: 177 Parzellen (221 Adressen), Spalten Prioritaet, Adresse, Parzelle, E-GRID, Mieter, Eigentuemer (leer), Hinweis. Prio 1 = 62, Prio 2 = 58, Prio 3 = 57. Keine Link-Spalte, weil SH kein Online-Eigentümerportal hat.
- `SH_Schaffhausen_Anleitung.txt`: SH ist ein Bestell-Kanton. Die Datei enthält einen Mailentwurf auf Deutsch an das Kantonale Grundbuchamt Schaffhausen, Mühlentalstrasse 105, 8200 Schaffhausen, 052 632 71 11, gbamt@sh.ch. Der Entwurf verlangt die Auskunft nach Art. 970 Abs. 2 ZGB, verweist auf die Liste in der Beilage und fragt vorab nach den Kosten. Nichts wurde versendet.
- **Verifizierung der Amtsadresse: teilweise.** Die Angaben stammen aus einem amtlichen Dokument der Stadt Stein am Rhein. Die BJ-Liste der Grundbuchbehörden nennt dieselbe Adresse, aber die alte Mail gbamt@ktsh.ch und die Nummer 052 632 74 01. sh.ch war während des Laufs im Wartungsmodus (HTTP 500 «Die Seite wird gerade gewartet»), deshalb ist keine Prüfung auf der Kantonsseite möglich. kantone_quellen.md (Zeile SH) ist entsprechend nachgeführt.

## Probleme
- sh.ch im Wartungsmodus, siehe oben. Bitte die Mailadresse vor dem Versand auf sh.ch prüfen.
- Kein Grundbuch- oder Eigentümerportal wurde abgefragt. Fremde untracked Dateien (tools/anfragen/, nachtlauf.sh, nachtauftrag_eigentuemer.md) wurden nicht committet.
- `tools/berichte/2026-11-08_register_abgleich.csv` wurde vom Abgleich neu geschrieben (bekannt, siehe Chur-Bericht).
