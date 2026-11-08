# Rapperswil (SG), Lauf 08.11.2026

## Strassen
Bestätigt (strassen_ok): Marktgasse, Hauptplatz (neu in CITIES), Fischmarktplatz, Untere Bahnhofstrasse, Obere Bahnhofstrasse, Halsgasse, Hintergasse, Kluggasse. Die sieben bestehenden CITIES-Strassen sind geblieben. Grundlage: topstrassen.py um die Altstadt (Ortssuche «Rapperswil-Jona» landete in Jona, darum mit Koordinate `Rapperswil@47.2265,8.8170`). Rathausstrasse, Zürcherstrasse und Fischmarktstrasse haben auch viele Läden, sind aber Neustadt bzw. Durchgangslage und wurden nicht aufgenommen.

## Adressen
- 140 Adressen: 119 aus OSM (adressen.py) und 21 EXTRA aus dem amtlichen Gebäudeverzeichnis (GWR über geo.admin). Hauptplatz (15 amtliche Nummern, OSM nur 1) und Fischmarktplatz (8, OSM 0) sind in OSM praktisch ohne Adressen.
- 4 OSM-Adressen fehlen im amtlichen Verzeichnis: Marktgasse 2 und 3, Obere Bahnhofstrasse 30 und 58. Ihre Parzelle wurde über die OSM-Koordinate bzw. die Nachtlauf-CSV bestimmt.

## Mieter
- 96 Adressen neu mit Mieter (135 Mieter-POIs). Viele Rapperswiler Läden haben in OSM keine Adresse. Sie wurden per Point-in-Polygon dem OSM-Gebäude zugeordnet, aber nur, wenn das Gebäude genau eine amtliche Adresse hat. Ausnahmen: Rössli/Banoo → Hauptplatz 5 und acrevis → Hauptplatz 6. Diese Gebäude haben noch eine zweite Adresse an der Strehlgasse, das steht in notes.
- Nicht zugeordnet (Gebäude mit mehreren Adressen ausserhalb der Strassen oder ohne Gebäude): unter anderem Albuville mit Tally Weijl, MAC, Bayard, Räber (Klaus Gebert Strasse 2/6), Marc O'Polo und Maria's Boutique (Merkurstrasse 1 / Rathausstrasse 8), Apotheke Dr. Stoffel (Obere Bahnhofstrasse 58a oder 58b).

## Eigentümer
- register_abgleich.py: 0 neue Treffer (5 Konflikte in anderen Städten, unverändert).
- Von Hand ergänzt: Obere Bahnhofstrasse 32b und 32c = UBS Sima (Halbjahresbericht 30.06.2026 nennt «Obere Bahnhofstr. 32 a, b, c», Parzelle 367 wie 32a). Der Abgleich hatte nur 32a erkannt. UIDs aus bestehenden Einträgen übernommen: UBS Fund Management CHE-102.674.664, Swiss Prime Anlagestiftung CHE-374.175.355.
- Hinweis ohne Eintrag als owner: Hauptplatz 1 vermutlich Rathaus, Eigentümerin laut Südostschweiz (22.12.2022) die Ortsgemeinde Rapperswil-Jona. Die Zuordnung der Adresse ist ungeprüft.
- Stand: 5 von 140 mit Eigentümer, **135 offen**.

## Parzellen
Für alle 137 Adressen ohne Eigentümer wurden Parzelle («Rapperswil <Nr>») und E-GRID in notes eingetragen. Quellen: Nachtlauf-CSV (03.11., geo.admin), parzelle.py für die 21 EXTRA-Adressen und das GWR für den Rest. Die E-GRIDs aus GWR und Kataster stimmen überein. Das GWR führt die Nummern mit «R» (Grundbuchkreis Rapperswil). Einzige Abweichung ist Marktgasse 3a: GWR 236R, Kataster 237, übernommen wurde der Kataster.

## Anfragelisten
- ~/Downloads/Retail Map Anfragen/SG_Rapperswil.csv: 125 Parzellen bzw. 135 Adressen, Priorität 1/2/3 = 25/67/33.
- ~/Downloads/Retail Map Anfragen/SG_Rapperswil_Anleitung.txt mit Mailentwurf an das Grundbuchamt Rapperswil-Jona, St. Gallerstrasse 23, Postfach 2160, 8645 Jona, 055 225 71 10. Am 08.11.2026 auf rapperswil-jona.ch verifiziert. Auf der Seite steht keine E-Mail-Adresse, nur ein Kontaktformular. Nichts versendet.

## Probleme
- Nominatim-Zentrum für «Rapperswil-Jona» liegt in Jona, darum Koordinate verwenden.
- Keine E-Mail-Adresse des Grundbuchamts öffentlich.
