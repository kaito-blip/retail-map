# Tageslauf 08.11.2026: La Chaux-de-Fonds (NE)

## Strassen
Avenue Léopold-Robert, Rue Neuve, Place du Marché, Rue de la Balance, Rue du Marché (bisher in CITIES, bleiben). **Neu:** Rue Daniel-JeanRichard, in CITIES zusätzlich die OSM-Schreibweisen «Rue Daniel-Jean Richard» und «Rue Daniel-Jeanrichard». `strassen_ok` steht jetzt auf true.
Ergebnis `topstrassen.py` (Radius 900 m): Avenue Léopold-Robert 8 Läden, Rue Daniel-JeanRichard 6 (+2 +1 in den anderen Schreibweisen), Rue Neuve 4, Rue Fritz-Courvoisier 3, Rue Jaquet-Droz 3, Promenade des Six-Pompes 3, Rue de la Balance 2, Rue de la Serre 2.
- Avenue Léopold-Robert («le Pod»): Hauptboulevard mit Läden, Banken und Gastronomie. Auf den Kern gekürzt, Nr. 7 bis 96 (bis vor den Grand-Pont). Nr. 100 bis 152 (Entilles Centre, Toyota, Shell) ist Ausfallstrasse und nicht dabei.
- Rue Daniel-JeanRichard: parallele Geschäftsstrasse mit Métropole Centre, Denner, Ochsner Sport, Sun Store.
- Rue Neuve, Place du Marché, Rue du Marché, Rue de la Balance: Altstadtkern um den Markt (Chocolaterie, Delikatessen, Gastronomie).
- Verworfen: Rue Fritz-Courvoisier, Rue Jaquet-Droz, Rue de la Serre (Durchgangs- bzw. Nebenlagen), Promenade des Six-Pompes (Wohnquartier mit Einzelläden).

## Zahlen
- **154 Adressen** aus OSM nach Kürzung (191 vor Kürzung): Léopold-Robert 81, Daniel-JeanRichard 23 + 3 + 2, Rue Neuve 15, Balance 15, Place du Marché 8, Rue du Marché 7.
- **4 amtliche Adressen, die in OSM fehlen**, aus dem GWR (geo.admin) als `EXTRA['La Chaux-de-Fonds']` ergänzt: Avenue Léopold-Robert 23, 61a, 88a, Rue de la Balance 6a. Lückenprüfung gegen GWR für alle sechs Strassen; OSM ist hier fast vollständig. Total **158 Keys**.
- **Neue Mieter:** 46 Adressen.
- **Register-Abgleich** (`register_abgleich.py --schreiben`): 0 neue, 1 bestätigt (Cronos Léopold-Robert 25).
- **Neue Eigentümer (1):** Avenue Léopold-Robert 23, Cronos Immo Fund (Cronos Finance SA, CHE-115.858.877, Pully), Rapport semestriel 31.03.2026, Liegenschaft «Avenue Léopold-Robert 23-25», gleiche Parzelle 10516 wie Nr. 25. UID und Sitz auch bei Nr. 25 ergänzt.
- **Parzelle und E-GRID** für alle 156 offenen Adressen gesetzt, aus dem GWR (lparz/egrid) und mit `parzelle.py` (amtliche Vermessung am Adresspunkt) gegengeprüft. Abweichungen:
  - Léopold-Robert 68, 70, 72, 74: Vermessung zeigt neue Parzellen 21080, 21079, 21078, 21077 ohne E-GRID, GWR noch die alten (5261, 3040, 3042, 5260). Neue Nummer gesetzt, alte in notes.
  - Léopold-Robert 59: GWR DP1269, Vermessung 19617 → 19617. Léopold-Robert 32 und 75a: Adresspunkt auf DP1508 bzw. DP1471, Gebäude laut GWR auf 11940 bzw. 8203 → GWR-Parzelle.
  - Léopold-Robert 38 (Fielmann) und 61a auf DP1446, Place du Marché 1 auf DP511 (laut GWR und Vermessung Strassenparzelle). Nur vermerkt, kein Eigentümer eingetragen.
  - OSM «13bis» = amtlich 13a, OSM «16;18» = Parzelle von Nr. 16, OSM «11 A» = 11a.
- **Eigentümer La Chaux-de-Fonds: 2 von 158, offen 156.**
- **SEED:** 6894 Einträge, 657 mit Eigentümer. Gegen den Stand vor dem Schreiben geprüft: kein Key verloren, kein bestehender Wert überschrieben, notes nur ergänzt. JS-Syntax geprüft.

## Anfrageliste
- `~/Downloads/Retail Map Anfragen/NE_La Chaux-de-Fonds.csv`: 126 Parzellen (156 Adressen), Spalten Prioritaet, Adresse, Parzelle, E-GRID, Mieter, Eigentuemer (leer), Link, Hinweis. Prio 1 = 26, Prio 2 = 87, Prio 3 = 13.
- Link-Spalte: SITN-Karte zentriert auf die Adresse (GeoMapFish-Permalink, nur aus dem Aufbau abgeleitet, nicht getestet).
- `NE_La Chaux-de-Fonds_Anleitung.txt`: Weg A SITN (gratis, Captcha je Abfrage, Kaito einzeln), Weg B Mailentwurf Französisch an SGRF registrefoncier@ne.ch (verifiziert 08.11.2026 auf ne.ch, aus dem Neuchâtel-Lauf übernommen). Nichts versendet.
- Die ältere Nachtlauf-Datei `Parzellen/NE_La_Chaux_de_Fonds.csv` (ungekürzte Léopold-Robert, ohne Daniel-JeanRichard) ist überholt.

## Probleme
- Keine Antworten in `Antworten/` für La Chaux-de-Fonds.
- OSM erfasst an der Avenue Léopold-Robert nur wenige Läden mit Namen (8 im Kern); die Mieterzahl ist deshalb tief, eine Begehung würde viel ergänzen.
- Kein Grundbuch- oder Eigentümerportal abgefragt, SITN nicht geöffnet. Fremde untracked Dateien (tools/anfragen/, nachtlauf.sh, nachtauftrag_eigentuemer.md) nicht committet.
