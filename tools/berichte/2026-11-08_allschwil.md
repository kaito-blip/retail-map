# Allschwil (BL), Lauf 08.11.2026

## Strassen
Allschwil hat keine klassische High Street. Die Läden verteilen sich auf die Hauptachse und zwei Einkaufscluster. Gewählt (staedte.json, `strassen_ok: true`):
- **Baslerstrasse** (ganz, Dorf bis Neuallschwil/Lindenplatz): Coop 28, Raiffeisen 70, UBS 96, Post 103, Gemeindeverwaltung 111, BLKB 172, Migros 191, Sutter Begg 310
- **Binningerstrasse** Nr. 1 bis 112: Fachmarktcluster Jumbo 74, Coop 84, Aldi/Interdiscount 86, Migrol 91
- **Spitzwaldstrasse** Nr. 180 bis 270: Einkaufszentrum Paradies (215: Migros, Denner, Amavita, Coiffina)
- **Dorfplatz** (Dorfkern)
- **Lindenplatz** (Neuallschwil, Tramschlaufe)

CITIES-Eintrag in index.html um Spitzwaldstrasse und Dorfplatz ergänzt; Hegenheimermattweg und Oberwilerstrasse bleiben drin (bestehend).

## Zahlen
- Adressen: 394 (Baslerstrasse 261, Binningerstrasse 86, Spitzwaldstrasse 25, Dorfplatz 15, Lindenplatz 7)
- Neue Mieter: 51 Adressen
- Neue Eigentümer: 0 (Register-Abgleich ohne neue Treffer; 9 Adressen der gewählten Strassen hatten schon Eigentümer aus dem Register: Baslerstrasse 252/254 SPA, 256/258/260 UBS Anfos, 262 UBS Sima, Binningerstrasse 11/13 Swisscanto IFCA, 95 Warteck)
- Offen: 385 Adressen, alle mit Parzelle und E-GRID im SEED
- Hinweis in notes: Baslerstrasse 111 vermutlich Einwohnergemeinde Allschwil, ungeprüft

## Anfragelisten
- `~/Downloads/Retail Map Anfragen/BL_Allschwil.csv`: 229 Grundstücke (Prio 1: 17, Prio 2: 136, Prio 3: 76) mit Direktlink https://eigentumsauskunft.geo.bl.ch/<E-GRID> und leerer Spalte Eigentuemer
- `BL_Allschwil_Anleitung.txt`: Portal mit Captcha (Kaito einzeln) plus Mailentwurf an Grundbuchamt BL, grundbuchamt@bl.ch (verifiziert 08.11.2026)

## Probleme
- Adressen per Gemeindefläche (Overpass-Area Allschwil) statt per Radius geholt, weil Binningen eine Baslerstrasse und Basel eine Binningerstrasse hat. `tools/adressen/allschwil.json` ist entsprechend gefiltert.
- Nachtlauf-CSV `Parzellen/BL_Allschwil.csv` hatte für Lindenplatz 1 die falsche Parzelle «84» (E-GRID CH687720687703, nicht Allschwil). Korrigiert per OSM-Koordinate auf A-1500 (CH690779443933). 351 Parzellen wurden aus der Nachtlauf-CSV übernommen, 43 neu über geo.admin bestimmt (6 davon per OSM-Koordinate).
- Kein Portal abgefragt, nichts versendet.
