# Porrentruy (JU), Lauf 08.11.2026

**Strassen** (`strassen_ok` jetzt true): Grand-Rue, Rue Pierre-Péquignat, Rue des Malvoisins, Allée des Soupirs, Rue du 23-Juin (Altstadt), neu Faubourg St-Germain.
Die fünf bisherigen CITIES-Strassen bleiben drin. Ergänzt habe ich zwei Einträge:
- **Rue Pierre Péquignat** (ohne Bindestrich): So lautet der amtliche Name und fast alle OSM-Adressen (28). Mit dem Bindestrich gibt es in OSM nur zwei Adressen (Nr. 1 La Gueule du Loup, Nr. 9 Hôtel des Halles). Ohne die Ergänzung hätte die Karte die Strasse praktisch leer gezeigt. Beide Schreibweisen bleiben drin, Doppelungen gibt es keine.
- **Faubourg St-Germain**: Hier liegen das Esplanade Centre (Nr. 2: Migros, Denner, ALDI, C&A, Tally Weijl, Chicorée, Dosenbach, Visilab, Sun Store, Swisscom, Sunrise, Naville u.a.) und die Coop (Nr. 3). Laut topstrassen.py ist das klar die ladenstärkste Strasse der Stadt.
Bewusst weggelassen habe ich Rue du Jura (Bahnhof, Post, Banken, Gastronomie), Route de Courgenay und Route de Courtedoux. Das sind Bahnhofs- und Ausfallachsen.
CITIES-q «Porrentruy» ist korrekt: Nominatim liefert zuerst relation 1685622 (Gemeinde).

**Adressen:** 144 Keys. 141 kommen aus OSM (Grand-Rue 42, Rue Pierre Péquignat 28 + 2, Faubourg St-Germain 24, Rue du 23-Juin 23, Rue des Malvoisins 14, Allée des Soupirs 8). Drei amtliche Adressen fehlen in OSM, ich habe sie als `EXTRA['Porrentruy']` ergänzt: Faubourg St-Germain 5a und 24a, Rue des Malvoisins 23. Nebeneingänge (13.1, 14.1, 22.1, 22.2) habe ich nicht aufgenommen.
Wegen der Courroux-Kollision in Delémont habe ich nicht adressen.py mit Radius verwendet. Die Abfrage lief mit derselben Logik direkt auf die Gemeindefläche (area 3601685622). Ergebnis in tools/adressen/porrentruy.json.
Die Läden im Esplanade Centre und in der Altstadt haben in OSM oft keine Adresse. Ich habe sie über das Gebäudepolygon der adressierten Gebäude zugeordnet (49 POIs). 20 POIs ohne Adresse liegen ausserhalb adressierter Gebäude und sind nicht zugeordnet, z.B. Banque Cantonale du Jura, Valiant, MAC Electroménager, L'Innovation, Le Panier d'Asie und Boutique Annabelle. Einige davon liegen an Nebenstrassen wie Rue Trouillat und Faubourg de France.

**Neue Mieter:** 45 Adressen. Neben den Esplanade-Mietern sind das u.a. Amavita (Malvoisins 1), pharmacie plus (Grand-Rue 2), Benu (23-Juin 2), Boulangerie Roelli, Chaussures L'Escarpin, Di Nolfi Chaussures, Esprit de Femmes, Brasserie des deux Clefs und Lion d'Or. Hôtel de Ville, Bibliothèques und Salle de l'Inter habe ich unverändert übernommen.

**Eigentümer:** Der Registerabgleich brachte für Porrentruy keinen Treffer, das Register kennt dort nur SBB-Liegenschaften an der Place de la Gare und La Rochette. Neue Eigentümer: 0.
Folgende Einträge stehen nur als Vermutung in notes, `owner` bleibt leer:
- Rue Pierre Péquignat 2 (Hôtel de Ville): vermutlich Commune de Porrentruy
- Rue Pierre-Péquignat 9 (Hôtel des Halles, BiCJ): vermutlich République et Canton du Jura
- Grand-Rue 5 (Bibliothèque municipale): vermutlich Commune de Porrentruy

**Parzellen:** Alle 144 Adressen haben Parzelle und E-GRID, zusammen 131 Parzellen. Die Werte kommen über geo.admin: Die Koordinaten stammen aus dem GWR, die Parzelle aus der Identify-Abfrage auf den Kataster, mit 1 Sekunde Pause. Bei drei Adressen, die nur in OSM stehen (Faubourg St-Germain 22c, Rue du 23-Juin 8, Rue des Malvoisins 9a), habe ich die Parzelle über den OSM-Punkt bestimmt. parzelle.py lieferte dort nichts oder einen Treffer in Les Breuleux.
Rue des Malvoisins 3, 5, 7, 9 und 13 liegen laut Kataster auf .A-Grundstücken (283.A bis 288.A, vermutlich DDP), das GWR nennt die Stammgrundstücke. Beides steht in notes. Rue des Malvoisins 9a liegt auf 3502.A.

**Offen:** 144 von 144 Adressen ohne Eigentümer.

**Anfrageliste:** ~/Downloads/Retail Map Anfragen/JU_Porrentruy.csv (144 Adressen, Spalten Adresse;Parzelle;E-GRID;Mieter) und JU_Porrentruy_Anleitung.txt mit französischem Mailentwurf an das Registre foncier JU (registre.foncier@jura.ch, am 08.11.2026 auf jura.ch verifiziert, siehe Lauf Delémont). Die Mail kann mit der Delémont-Anfrage gebündelt werden. Nichts wurde versendet.

**Probleme:** OSM ist in Porrentruy dünn erfasst, und viele Läden haben keine Adresse. Eine Begehung würde viel mehr Mieter bringen. Kein Grundbuch- oder Eigentümerportal wurde abgefragt. Antworten von Kaito lagen keine vor, der Ordner Antworten existiert nicht.
