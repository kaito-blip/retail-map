# Wädenswil (ZH), Lauf 09.11.2026

## Strassen
Bisher in CITIES: Zugerstrasse, Seestrasse, Oberdorfstrasse, Florhofstrasse, Türgass (bleiben drin).
Neu ergänzt nach `topstrassen.py "Wädenswil" 15 600`: **Gerbestrasse** (11 Läden, zweitstärkste Strasse im Zentrum, McOptic, Buri Sport, Claro).

Filter in tools/adressen/w_denswil.json: Zugerstrasse nur Nr. 1 bis 41, Seestrasse nur Nr. 77 bis 139 (Bahnhofbereich). Die übrigen Abschnitte sind Wohn- und Gewerbegebiet oder Ausfallstrasse. Seestrasse 96 bis 116 und «93,95» aus dem 2500-m-Radius liegen rund 2,3 km entfernt; 96, 106 und 108 sind per Gemeindefläche geprüft und liegen nicht in Wädenswil, die übrigen sind aus der Distanz abgeleitet. Die Karte zeigt weiterhin alle Adressen dieser Strassen in der Gemeinde.

## Zahlen
- Adressen: 137 (Seestrasse 33, Zugerstrasse 28, Florhofstrasse 25, Oberdorfstrasse 22, Türgass 20, Gerbestrasse 9)
- Neue Mieter (tenant): 44 Adressen
- Parzelle und E-GRID (geo.admin): 135 von 135 offenen Adressen, alle in 8820 Wädenswil, keine Abweichung zur Nachtlauf-CSV. Zugerstrasse 6 (Coop, Dosenbach) fehlt im amtlichen Adressverzeichnis, Parzelle WE8084 per OSM-Koordinate bestimmt.
- Neue Eigentümer: 0. Register-Abgleich vor und nach dem Parzellen-Schritt ohne neue Treffer.
- Im Kern bereits erfasst: Oberdorfstrasse 28 und 30 (Swiss Prime Anlagestiftung, Parzelle WE6151), UID CHE-374.175.355 und Sitz Olten aus Zefix ergänzt. Ausserhalb des Kerns bleiben Seestrasse 23, 205 und 219 aus dem Register unverändert im SEED.
- Hinweise «vermutlich …, ungeprüft» (nur in notes):
  - Seestrasse 81 (WE5110): Stadt Wädenswil, Kauf vom Kanton Zürich laut RRB Nr. 483/2013. Der Beleg ist von 2013, der heutige Stand wurde nicht bestätigt, darum kein Eintrag in owner.
  - Florhofstrasse 6 (WE13466): Stadt Wädenswil, Sitz der Stadtverwaltung.
- Offen: 135 Adressen auf 112 Parzellen

## Anfragelisten
- `~/Downloads/Retail Map Anfragen/ZH_Wädenswil.csv`: 112 Parzellen, Prio 1: 32, Prio 2: 30, Prio 3: 50. Spalten Hinweis und Eigentuemer, keine Link-Spalte (ZH-Portal verwirft Koordinaten, siehe Winterthur).
- `~/Downloads/Retail Map Anfragen/ZH_Wädenswil_Anleitung.txt`: GIS-Browser ZH (SMS, ca. 5 pro Tag, Kaito fragt selbst einzeln ab) und Mail-Entwurf an das Notariat, Grundbuch- und Konkursamt Wädenswil, Zugerstrasse 16, 8820 Wädenswil, 044 859 25 50, waedenswil@notariate-zh.ch. **Verifiziert** am 09.11.2026 auf notariate-zh.ch/de/ihr-notariat/waedenswil. Nichts versendet.

## Probleme
- Keine Antworten in `Retail Map Anfragen/Antworten/` vorhanden (Ordner existiert nicht).
- Das Notariat ist am 12. und 13.11.2026 wegen eines IT-Systemwechsels geschlossen, ab 16.11. wieder offen.
- Drittquellen nennen andere Telefonnummern und Zuständigkeiten (law.ch 044 783 86 20; ein Verzeichnis zusätzlich Hütten und Schönenberg). In der Anleitung steht nur der Stand der Amtsseite.
- Seestrasse 185 bis 200 (McDonald's, Migrolino, Stöckli) und Zugerstrasse 56 liegen ausserhalb des Kerns und wurden nicht aufgenommen.
- Bekannte Eigennutzer wie Coop (Zugerstrasse 6), Migros (Oberdorfstrasse 27), ZKB (Zugerstrasse 12) sind nicht belegt und wurden nicht eingetragen. Eine Websuche ergab dazu nichts.
