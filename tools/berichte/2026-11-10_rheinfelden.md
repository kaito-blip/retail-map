# Rheinfelden (AG), Lauf 10.11.2026

## Strassen
Marktgasse, Kaiserstrasse, Bahnhofstrasse, Kupfergasse, Fröschweid (bestehend), neu Geissgasse.
Die Adressen stammen aus der Gemeindefläche (OSM-Relation 1684403), nicht aus dem Radius von adressen.py, wegen Rheinfelden (Baden) und der Nachbargemeinden. `topstrassen.py` zählt Friedrichplatz, Alte Landstraße und Lindenstrasse mit dem Radius, davon sind die ersten zwei Baden (D).
Kandidat für später: Brodlaube (rund 15 kleine POIs, Coiffeur, Massage, Bestattung, keine Filialen), nicht aufgenommen. Baslerstrasse (Valiant, Raiffeisen, TopPharm) ist Ausfallstrasse.

## Ergebnis
- Adressen: 166 (Marktgasse 67, Kaiserstrasse 27, Geissgasse 21, Bahnhofstrasse 20, Kupfergasse 18, Fröschweid 13)
- Adressen mit Mieter: 79, davon 78 neu. 71 POIs ohne Adresse wurden per OSM-Gebäudeumriss einer Adresse zugeordnet (Hinweis in notes).
- Parzelle und E-GRID: alle 166 (geo.admin, 162 über die Adresse, 4 per OSM-Koordinate: Marktgasse 10, 18, Bahnhofstrasse 8, Kupfergasse 7).
- Eigentümer: 4 von 166, davon 1 neu.
  - Neu Marktgasse 12 (Haus zur Sonne): Stiftung Fricktaler Museum Rheinfelden, CHE-255.941.232. Schenkung durch die Einwohnergemeinde, Rechnung 2025 in der Botschaft EWG vom 17.06.2026.
  - Bestand aus dem Register: Marktgasse 36 und 38 (Pensimo Casareal), Bahnhofstrasse 21 (Realstone RSF). UID und Sitz ergänzt.
- Offen: 162 Adressen auf 141 Parzellen.

## Nur als Hinweis in notes (nicht als Eigentümer)
- Marktgasse 16 (Rathaus), Bahnhofstrasse 20 (Schulhaus Hugenfeld), Kaiserstrasse 34 (Kloos): vermutlich Einwohnergemeinde.
- Marktgasse 10: Stadt hat 2013 Stockwerkeigentum für die Stadtbibliothek gekauft, übrige Einheiten offen.
- Bahnhofstrasse 19 und Marktgasse 60: vermutlich Schützen Rheinfelden Immobilien AG (CHE-108.062.117). Das Porträt von Lienhardt & Partner war nicht abrufbar (404, HTML-Antwort), Quelle nur Suchtreffer.

## Anfrageliste
`~/Downloads/Retail Map Anfragen/AG_Rheinfelden.csv` (162 Zeilen, Prio 1: 55, Prio 2: 40, Prio 3: 67, mit Kartenlink) und `AG_Rheinfelden_Anleitung.txt` mit Portalweg und fertiger Mail an das Grundbuchamt Laufenburg. Nichts versendet.
Grundbuchamt Laufenburg ist jetzt verifiziert: E-Mail und Telefon stehen auf ag.ch in den strukturierten Seitendaten (JSON-LD).

## Probleme und Besonderheiten
- OSM führt «Kupfergase» (Tippfehler) neben «Kupfergasse». Die Mieter stehen unter den amtlichen Kupfergasse-Keys, Nr. 7 liegt in EXTRA. «Kupfergase» steht bewusst nicht in CITIES, sonst gäbe es doppelte Marker.
- Bahnhofstrasse 21: Die Stadt plant laut Budget 2026 einen Projektwettbewerb Bahnhofsaal, in OSM heisst das Gebäude Bahnhofsaal. Realstone-Eintrag bleibt, Verhältnis ungeprüft.
- Mieter-Zuordnung teils unsicher: Froh Natur und Aglio & Olio (Geissgasse 7/9) sowie Chicorée und Toni's Marktplatz (Marktgasse 10/10a) wurden der Haupt- bzw. höheren Hausnummer zugeordnet. Altstadt-Papeterie steht in OSM an 29 und 32. Kurzhaarschnitt und Albrechtli Bar (Geissgasse 6 oder Albrechtsplatz 4) sind nicht eingetragen.
- register_abgleich hat beim Lauf 20 neue Register-Treffer in anderen Städten eingetragen (Zuger PK, PK Thurgau, Stadt Winterthur aus der Register-Runde 3), für Rheinfelden keine neuen.
- Im Arbeitsbaum lagen 9 fremde uncommittete Zürcher Einträge (Bahnhofstrasse). Sie bleiben ausserhalb dieses Commits.
- Antworten/: keine Dateien, keine `_nicht_zugeordnet_*.csv`.
