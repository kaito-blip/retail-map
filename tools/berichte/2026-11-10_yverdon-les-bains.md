# Yverdon-les-Bains (VD), Lauf 10.11.2026

## Strassen
Rue du Lac, Rue du Milieu, Rue de la Plaine, Place Pestalozzi, Rue du Casino (bestehend), neu Rue du Four (`topstrassen.py`: 10 Läden, 12 total).
Die Adressen stammen aus der Gemeindefläche (OSM-Relation 1868691, admin 8, BFS 5938), nicht aus dem Radius von adressen.py, um Nachbargemeinden auszuschliessen. Die gleichnamige Relation 1685206 ist admin 9.

## Ergebnis
- Adressen: 239 (Rue de la Plaine 81, Rue du Milieu 47, Rue du Lac 45, Rue du Four 39, Place Pestalozzi 18, Rue du Casino 9). 15 davon aus dem GWR per EXTRA, weil sie in OSM fehlen.
- Mieter: 147 Adressen mit Mieter, davon 145 neu. 112 Läden ohne Hausnummer wurden per OSM-Gebäudeumriss oder Nähe zugeordnet (Hinweis in notes, ungeprüft).
- Parzelle und E-GRID: alle 239 (GWR und amtliche Vermessung, geo.admin; 5 nur per OSM-Koordinate).
- Eigentümer: 7 von 239, davon 2 neu.
  - Neu Place Pestalozzi 15 und 16 (Château, Parzelle 1920): Commune d'Yverdon-les-Bains. Quelle: Préavis PR25.34PR Château étape XXIX, Données du cadastre.
  - Bestand aus dem Register: Rue du Lac 1 und 3, Rue du Milieu 2 und 4 (Akara Diversity PK, Parzelle 1898), Rue du Lac 49 (Patrimonium AST). UID und Sitz aus Zefix ergänzt (Swiss Prime Site Solutions AG CHE-211.793.771, Patrimonium Anlagestiftung CHE-115.158.366).
- Offen: 232 Adressen auf 188 Parzellen.

## Nur als Hinweis in notes (nicht als Eigentümer)
Vermutlich Commune d'Yverdon-les-Bains, ungeprüft: Place Pestalozzi 1 und 2 (Hôtel de Ville, Parzelle 1919, dort auch Rue du Four 1), Rue du Four 5 (Préavis PR24.25PR, parc immobilier communal), Rue du Casino 8 (nur Dateiname eines Avis d'enquête, PDF 404), Rue du Casino 9 (Théâtre Benno Besson, Kredite der Stadt, Eigentum nicht ausdrücklich genannt).

## Anfrageliste
`~/Downloads/Retail Map Anfragen/VD_Yverdon-les-Bains.csv` (188 Zeilen, Prio 1: 29, Prio 2: 106, Prio 3: 53, mit Kartenlink, ohne Portal-Direktlink) und `VD_Yverdon-les-Bains_Anleitung.txt` mit Portalweg Intercapi (5 Parzellen pro Tag, SMS) und fertiger Mail an das Office Broye-Nord vaudois. Nichts versendet.
Registre foncier Broye-Nord vaudois ist verifiziert auf vd.ch (rf.yverdon(at)vd.ch, Rue de Neuchâtel 1). Die Seite nennt den District Jura-Nord vaudois, nicht die Gemeinde einzeln.

## Probleme und Besonderheiten
- OSM führt Rue du Milieu 24 bis und 24b getrennt, amtlich gibt es nur 24b. Beide bleiben als Marker, die Mieter stehen an 24 bis. Weitere bis-Formen in OSM (Rue de la Plaine 58 bis, Rue du Four 4bis, 23bis) entsprechen amtlich 58b, 4b, 23b.
- Nur in OSM, nicht im GWR: Place Pestalozzi 15 und 16, Rue du Casino 5 und 6, Rue du Four 17 (amtlich 17a/17b per EXTRA). Parzellen aus der OSM-Position.
- Rue du Four 19: E-GRID aus GWR (CH229772834589) weicht von der amtlichen Vermessung ab (CH438397457382), Parzelle 1976 in beiden. AV verwendet.
- Stadt-PDFs (Préavis, Rapport de gestion) lieferten nur beim Château einen ausdrücklichen Eigentümer. Ein Inventar der Stadt wurde nicht gefunden.
- register_abgleich: keine neuen Treffer, die 5 Konflikte betreffen Bern und Zürich, nicht Yverdon.
- Im Arbeitsbaum lagen 9 fremde uncommittete Zürcher Einträge. Sie bleiben ausserhalb dieses Commits.
- Antworten/: keine Dateien, keine `_nicht_zugeordnet_*.csv`.
