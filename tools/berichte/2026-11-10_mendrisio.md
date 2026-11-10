# Mendrisio (TI), Lauf 10.11.2026

## Strassen
Via Luigi Lavizzari, Corso Bello, Via Stefano Franscini, Piazzale alla Valle (aus CITIES übernommen), neu Via Angelo Maspoli (FoxTown, Jumbo, Casinò) und Via Giuseppe Motta (10 Läden laut OSM, zweitstärkste Strasse).
Via Vincenzo Vela aus dem Vorschlag in staedte.json gestrichen: nur 2 Läden und 12 Adressen in Rancate.

## Adressen
120 Adressen: Via Giuseppe Motta 51, Via Luigi Lavizzari 20, Via Stefano Franscini 19, Corso Bello 16, Via Angelo Maspoli 14. Alle innerhalb der Gemeindefläche (OSM-Relation 2888450). Piazzale alla Valle: 0 Adressen, die Strasse fehlt im amtlichen Verzeichnis und in OSM.
GWR-Abgleich: keine fehlenden Hausnummern, kein EXTRA nötig. Via Giuseppe Motta 7 und 9 stehen in OSM als «7;9». Via Angelo Maspoli 13 und Via Stefano Franscini 29b stehen nur in OSM; ihre Parzellen stammen vom OSM-Punkt.

## Mieter
42 Adressen neu mit Mieter, zusammen 43 mit Mieter. Dazu 12 Läden ohne OSM-Hausnummer über das Gebäude zugeordnet (Via Luigi Lavizzari 2: Migros, Post, k kiosk, House Tech, Sirienne Margot, Bar Cerutti; Via Giuseppe Motta 26; Via Stefano Franscini 16; Via Luigi Lavizzari 28; Via Angelo Maspoli 7). Läden in Gebäuden mit mehreren Adressen sind nur als Hinweis in der Anfrageliste vermerkt.

## Eigentümer
5 von 120 mit Eigentümer, davon 2 neu, **115 offen**.

- Neu: Via Stefano Franscini 10 und 16 = UBS Residentia (Jahresbericht per 30.06.2026, S. 28, dort «Via Franscini 10, 16»). Von Hand eingetragen, weil der Abgleich die Kurzform nicht trifft. Beide Nummern liegen auf Parzelle 1227, und im Strassenverzeichnis gibt es in der Gemeinde nur eine Franscini-Strasse.
- Bestätigt: Via Stefano Franscini 3, 9, 11 = SBB (Parzelle 325, OGD); UID und Sitz ergänzt.
- UID und Sitz von UBS Fund Management und SBB aus bestehenden, per Zefix geprüften Einträgen übernommen, nicht neu abgefragt.
- Websuche zu FoxTown, Migros und Jumbo: kein Eigentümer belegt. Nur Vermarkter aus Inseraten in notes (Via Angelo Maspoli 21 Interfida SA, Via Luigi Lavizzari 21 Sequoia Consulting Sagl), ungeprüft.
- Kein Portal abgefragt. Der Antworten-Ordner war leer, es gibt keine `_nicht_zugeordnet`-Datei.

## Anfrageliste
`~/Downloads/Retail Map Anfragen/TI_Mendrisio.csv`: 91 Parzellen, 115 Adressen (Priorität 1: 38, 2: 19, 3: 34). `TI_Mendrisio_Anleitung.txt` mit italienischer Mail an das Ufficio del registro fondiario di Mendrisio, nichts versendet.
Amtsadresse verifiziert am 10.11.2026 auf www4.ti.ch (Via Pollini 29, 6850 Mendrisio, di-rf.mendrisio@ti.ch). Die Seite nennt keine Gemeinden, die Zuständigkeit ist aus dem Amtsnamen abgeleitet. In `tools/kantone_quellen.md` ergänzt.

## Probleme
1. **Fremde Änderungen in index.html.** Beim Lauf lagen 9 uncommittete Einträge Zürich Bahnhofstrasse im Arbeitsbaum (2, 13, 17, 18, 20, 35, 37, 41, 46; Eigentümer aus Grundbuchauskunft, teils Privatpersonen), die nicht aus diesem Lauf stammen. Sie sind nicht mitcommittet und liegen weiter unverändert im Arbeitsbaum; sie müssen separat committet werden.
2. `register_abgleich.py --schreiben` lief über alle Städte: 3 neue Eigentümer ausserhalb Mendrisios (Olten Baslerstrasse 144 und 160, Solothurn Hauptgasse 70, alle Kanton Solothurn, OGD) sind mitcommittet. 5 Konflikte (Bern Spitalgasse 2, Zürich Bahnhofstrasse 82, 82a, 86, 92) wurden nicht überschrieben, siehe `2026-11-10_register_abgleich.csv`.
3. Via Giuseppe Motta wurde ganz aufgenommen und ist zwischen den Ladengruppen stark Wohnstrasse. Deshalb steht sie ohne Mieter auf Priorität 3.
4. `Parzellen/TI_Mendrisio.csv` aus dem Nachtlauf basiert auf einer älteren Strassenwahl.
5. Im Log steht der Hinweis, dass die Claude-Anmeldung spätestens am 12.11.2026 enden kann. Für den Nachtlauf `claude auth login` oder `claude setup-token` nötig.
