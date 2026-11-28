# Folgelauf 28.11.2026: Neuchâtel (NE)

Die Stadt wurde schon am 08.11.2026 bearbeitet. Deshalb lief heute nur Schritt 4 (Eigentümer) für die offenen Adressen.

## Strassen (unverändert)
Rue du Seyon, Rue de l'Hôpital, Rue du Bassin, Rue Saint-Maurice, Rue du Temple-Neuf, Rue du Trésor, Grand-Rue / Grand Rue.

## Zahlen
- **120 Adressen** (Keys) in Neuchâtel, keine neuen Adressen, **keine neuen Mieter** (Schritt 2 und 3 nicht wiederholt).
- **Register-Abgleich** (`register_abgleich.py --schreiben`): 0 neue Eigentümer, 7 bestätigt (Bonhôte Hôpital 15 und Temple-Neuf 11, UBS 1a Immo PK Hôpital 20, La Foncière Hôpital 3/5, Mobimo Seyon 12, ERRES Saint-Maurice 4). Mobimo Seyon 12 kam schon am 13.11. aus der Register-Runde 4 dazu.
- **Neue Eigentümer (2):**
  - Rue du Seyon 25: **Ville de Neuchâtel** (Öffentliche Hand). Quelle ist der Rapport d'information 23-026 der Stadt zur Stratégie immobilière, S. 19 und 77. Dort ist das «bâtiment sis rue du Seyon 25» als sanierter Pilotbau des patrimoine financier der Ville genannt, im Abschnitt über die «biens propriétés de la Ville».
  - Rue du Seyon 23: Ville de Neuchâtel über dieselbe Parzelle Neuchâtel 12264. Das ist dieselbe Zuordnung über die Parzelle wie beim Lauf vom 08.11. Das Grundbuch wurde nicht geprüft.
- **Hinweis ohne Eintrag:** Rue du Trésor 4 (Maison des Halles). In notes steht «vermutlich Ville de Neuchâtel, ungeprüft». Die Ville saniert das îlot des Halles ab Frühling 2026 (Keystone-ATS/La Télé 21.01.2026, immobilier.ch), das Eigentum ist dort aber nicht ausdrücklich genannt.
- **Eigentümer Neuchâtel: 11 von 120, offen 109.** SEED gesamt 13'503 Einträge, 2'203 mit Eigentümer.
- Parzelle und E-GRID waren für alle offenen Adressen schon gesetzt (Lauf 08.11.), parzelle.py war nicht nötig.

## Anfrageliste
- `tools/anfragen/NE_Neuchâtel.csv`: 95 Parzellen für 109 Adressen. Prio 1 = 13, Prio 2 = 70, Prio 3 = 12. Spalten Prioritaet, Adresse, Parzelle, E-GRID, Mieter, Eigentuemer (leer), Link (SITN-Karte auf Adresse zentriert, Muster ungetestet, 1 Zeile ohne Link), Hinweis.
- `tools/anfragen/NE_Neuchâtel_Anleitung.txt`: Weg A ist SITN mit Captcha je Abfrage, Kaito fragt selbst einzeln ab. Weg B ist ein französischer Mailentwurf an den SGRF, registrefoncier@ne.ch (verifiziert 08.11.2026). **Nichts versendet.**
- Die Dateien liegen nicht in ~/Downloads (siehe Probleme). Sie sind nicht committet, weil der Mailentwurf die Absender-Mail enthält. Kaito bitte nach `~/Downloads/Retail Map Anfragen/` kopieren.

## Probleme
- **~/Downloads im Nachtlauf gesperrt** (macOS, `Operation not permitted`). Folgen:
  - `antworten_einlesen.py` brach beim Start ab (Log 2026-11-28.log). Antworten wurden daher nicht eingelesen, `_nicht_zugeordnet_*.csv` sind nicht lesbar und darum hier nicht gemeldet.
  - `register_abgleich.py` hing beim Zugriff auf `Downloads/.../Parzellen`. Ich habe den Lauf abgebrochen und ihn mit einem leeren Parzellen-Ordner neu gestartet. Für Neuchâtel fehlt dadurch nichts, alle Adressen stehen im SEED.
- Der Abgleich hatte bei 3 fremden Keys Notizen ergänzt (Luzern Grendelstrasse 15/19, das ist der bekannte Sima-Konflikt, und Genf Rue de la Rôtisserie 8). Ich habe sie zurückgesetzt. Committet sind nur die Neuchâtel-Änderungen.
- WebFetch wurde für neuchatelville.ch, immobilier.ch und latele.ch vom Proxy abgewiesen. Die Quellen habe ich deshalb per curl gelesen.
- Kein Grundbuch- oder Eigentümerportal abgefragt.
