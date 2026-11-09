# Bellinzona, Lauf 09.11.2026

## Strassen
Bestätigt (strassen_ok): Viale Stazione, Piazza Collegiata, Via Nosetto, Piazza Nosetto, Via Camminata (alle bisher in CITIES) und neu **Via Teatro**. Das sind sechs Strassen statt vier bis fünf, weil bestehende Strassen nicht entfernt werden.

## Adressen
102 Adressen (Viale Stazione 49, Via Camminata 19, Piazza Collegiata 14, Via Teatro 8, Piazza Nosetto 7, Via Nosetto 5).

- Abgleich OSM mit dem GWR. 20 amtliche Adressen fehlen in OSM und stehen jetzt als EXTRA in index.html (Piazza Collegiata 13, Piazza Nosetto 7).
- Nur in OSM, nicht im GWR: Viale Stazione 17 (GWR kennt 17a und 17b). Parzelle über die OSM-Position.
- `adressen.py` (Radius 2500 m) holte auch Giubiasco. `tools/adressen/bellinzona.json` enthält die bereinigte Auswahl (nur 6500 Bellinzona).

## Mieter
36 Adressen neu mit Mieter, 39 von 102 haben jetzt einen. POIs ohne Adresse sind per Point-in-Polygon dem Gebäude zugeordnet, nur wenn das Gebäude genau eine Adresse hat.

Nicht eingetragen, Hinweis in notes und Anfrageliste:
- Gebäude mit mehreren Adressen: Post und K Kiosk (Viale Stazione 16a/18/18a/18b/18c), Chiosco Emman (29a/29b), Bar della Posta (17/17b), Ottica Martini, immoprogramm, Intimissimi (4/6), k kiosk und Kuoni (Piazza Collegiata 7/7a), Rado Tettamanti (Piazza Collegiata 6/7a), Gelateria Veneta und Pennyblack (Piazza Collegiata 2/3), Monn (Piazza Collegiata 4, Via Magoria 3), Mackea und Toni Balocchi (Via Camminata 2/4), Amplifon (Via Teatro 2, Vicolo Muggiasca 1/1a).
- Grossblock Piazza Nosetto (1862 m², POIs 34 bis 59 m von der Adresse): Brums, Trend Coiffeure, Rocco Finelli, Bar Cervo, Bottega del Mondo.
- Kirche Piazza Collegiata 20 ist kein Mieter und wurde herausgefiltert.

## Eigentümer
0 neu, Stand 10 von 102 mit Eigentümer, **92 offen**.

- register_abgleich.py, zwei Läufe (der zweite als Trockenlauf nach den Parzellen): keine neuen Treffer. Bereits eingetragen: Viale Stazione 19 (Swiss Prime Anlagestiftung), 21 und 23 (Swisscanto Anlagestiftung), 30 (UBS Residentia), 36 bis 36e (SBB).
- UID und Sitz für diese 10 aus bestehenden, per Zefix geprüften Einträgen übernommen, nicht neu abgefragt.
- Websuche (Manor, Piazza Collegiata/Viale Stazione, Zuständigkeit RF): keine belegten Eigentümer gefunden.
- Viale Stazione 5: GWR-Gebäudebezeichnung «Manor», deshalb nur «vermutlich Manor AG, ungeprüft» in notes. Manor kann auch nur Mieterin sein.
- Portale: keines abgefragt. Antworten-Ordner enthielt keine Bellinzona-Datei.

## Anfrageliste
`~/Downloads/Retail Map Anfragen/TI_Bellinzona.csv` mit 69 Parzellen und 92 Adressen (Priorität 1: 42, 2: 17, 3: 10) und `TI_Bellinzona_Anleitung.txt` mit italienischer Mail an das Ufficio del registro fondiario di Bellinzona. Nichts versendet.

Amtsadresse verifiziert am 09.11.2026 auf www4.ti.ch (Via Bellinzona 31, 6512 Giubiasco, di-rf.bellinzona@ti.ch). Die Seite nennt keine Gemeinden, die Zuständigkeit ist aus dem Amtsnamen abgeleitet. In `tools/kantone_quellen.md` ergänzt.

## Probleme
1. **Viale Stazione gibt es zweimal.** Die Fusionsgemeinde hat sie in 6500 Bellinzona und in 6512 Giubiasco mit teils gleichen Hausnummern (23 Keys doppelt). Der SEED-Key kennt keine PLZ, alle Einträge gelten für 6500 und tragen dazu eine Notiz.
   - Die Karte zeigt bei Viale Stazione 1, 11 und 16 den Punkt in Giubiasco, die Daten gelten aber für 6500.
   - 12 Nummern gibt es in OSM nur in Giubiasco (1a, 3c, 5a, 7, 11a bis 11d, 20, 22, 24, 30a). Sie erscheinen auf der Karte als leere Punkte und wurden nicht erfasst.
   - Beheben lässt sich das nur im Kartencode, etwa mit einem PLZ-Filter pro Stadt. Das war nicht Teil des Auftrags.
2. **Viale Stazione 30 hat vermutlich die falsche Parzelle.** Im SEED steht «Bellinzona 306», E-GRID CH640702887689, laut SBB-OGD eine SBB-Parzelle in Giubiasco. GWR und Vermessung nennen für 6500 Bellinzona Parzelle 3756, E-GRID CH440702871329. Nicht überschrieben, Hinweis in notes. Die Registerzeile von UBS Residentia nennt nur «Bellinzona», welche Liegenschaft gemeint ist, bleibt ungeprüft. Bitte beim Grundbuch mitklären; die Adresse steht nicht in der Anfrageliste.
3. **Parzellen/TI_Bellinzona.csv aus dem Nachtlauf** enthält an der Viale Stazione Parzellen aus Giubiasco und sollte nicht verwendet werden. Parzellennummern gelten in Bellinzona je Grundbuchsektion, deshalb zählt das E-GRID.
4. `register_abgleich.py --schreiben` lief über alle Städte: 0 neue Eigentümer, die Abgleichliste wurde neu erzeugt.
