# Tageslauf 08.11.2026: Neuchâtel (NE)

## Strassen
Rue du Seyon, Rue de l'Hôpital, Rue du Bassin, Rue Saint-Maurice, Rue du Temple-Neuf (bisher in CITIES, bleiben). **Neu:** Rue du Trésor, Grand-Rue und die OSM-Variante «Grand Rue». `strassen_ok` steht jetzt auf true.
Ergebnis `topstrassen.py` (Radius 900 m): Rue du Seyon 14 Läden, Faubourg du Lac 4, Rue de l'Hôpital 3, Rue des Moulins 4, Faubourg de l'Hôpital 3, Rue du Trésor 3, Rue des Sablons 3, Rue de l'Ecluse 2, Grand Rue 2. OSM ist in Neuchâtel dünn erfasst, die Zahlen sind tief.
- Rue du Seyon: Hauptachse der Fussgängerzone (Payot, Laederach, Acuitis, Dessange).
- Rue de l'Hôpital: Fussgängerzone (Salt, McDonald's, Nature & Découvertes, Marionnaud).
- Rue du Bassin, Rue Saint-Maurice, Rue du Temple-Neuf: Fussgängerzone zwischen Seyon und Place Pury.
- Rue du Trésor und Grand-Rue: Altstadtgassen der Fussgängerzone mit Läden und Gastronomie (Fielmann, Mister Minit). OSM führt die Grand-Rue unter zwei Schreibweisen, deshalb beide in CITIES.
- Verworfen: Faubourg du Lac, Faubourg de l'Hôpital, Rue des Sablons, Rue de l'Ecluse (Durchgangs- oder Wohnstrassen, Nebenlagen), Rue des Moulins (Nebenlage).

## Zahlen
- **90 Adressen** aus OSM (Seyon 39, Hôpital 11, Grand-Rue 11 + 5, Trésor 9, Saint-Maurice 7, Bassin 6, Temple-Neuf 2).
- **30 amtliche Adressen, die in OSM fehlen**, über das amtliche Adressverzeichnis (geo.admin) gefunden und als `EXTRA['Neuchâtel']` in index.html ergänzt, darunter Rue du Bassin 6 bis 18, Rue de l'Hôpital 3, 5, 8 bis 14, 19, 22, Saint-Maurice 1, 5, 11, 13, 14, Temple-Neuf 1, 3, 5. Total 120 Keys.
- **Neue Mieter:** 28 Adressen (bei 3 stand schon ein Mieter).
- **Register-Abgleich** (`register_abgleich.py --schreiben`): 0 neue, 4 bestätigt (Bonhôte Hôpital 15 und Temple-Neuf 11, UBS 1a Immo PK Hôpital 20, ERRES Saint-Maurice 4).
- **Neue Eigentümer (4):**
  - Rue de l'Hôpital 3 und 5: La Foncière (Investissements Fonciers SA, CHE-100.981.285), Rapport semestriel 31.03.2026, Liegenschaft «Rue de l'Hôpital 3 – 5». Der Abgleich hatte sie nicht, weil beide Nummern in OSM fehlen.
  - Rue de l'Hôpital 22: UBS (CH) Property Fund Direct 1a Immo PK, über die gemeinsame Parzelle 2538 mit Hôpital 20.
  - Rue Saint-Maurice 10: ERRES Compartiment Swiss, über die gemeinsame Parzelle 9190 mit Saint-Maurice 4.
- **UID und Sitz aus Zefix** ergänzt: UBS Fund Management (Switzerland) AG CHE-102.674.664 (Basel), Edmond de Rothschild Real Estate SICAV CHE-217.800.369 (Vernier), Bonhôte-Immobilier SICAV CHE-396.569.515 (Neuchâtel), Investissements Fonciers SA CHE-100.981.285 (Lausanne).
- **Parzelle und E-GRID** für alle 116 Adressen ohne vorherige Parzelle gesetzt. 12 Adresspunkte lagen auf einer Strassenparzelle (DP24, DP299, DP300, DP301, DP304, DP836, DP861) und wurden auf die angrenzende Parzelle umgelegt (Hinweis in notes und CSV). Rue du Seyon 24b, 24c, 7a, Rue du Trésor 2 bis und Rue Saint-Maurice 0 stehen nicht im amtlichen Adressverzeichnis, die Parzelle kommt dort vom OSM-Punkt.
- **Eigentümer Neuchâtel: 8 von 120, offen 112.**
- **SEED:** 3000 Einträge, 621 mit Eigentümer. Gegen den Stand vor dem Lauf geprüft: kein Key verloren, kein bestehender Wert überschrieben, notes nur ergänzt. JS-Syntax geprüft.

## Anfrageliste
- `~/Downloads/Retail Map Anfragen/NE_Neuchâtel.csv`: 97 Parzellen (108 Adressen, Grand-Rue-Doppelschreibweisen zusammengefasst), Spalten Prioritaet, Adresse, Parzelle, E-GRID, Mieter, Eigentuemer (leer), Link, Hinweis. Prio 1 = 23, Prio 2 = 61, Prio 3 = 13.
- Link-Spalte: SITN-Karte zentriert auf die Adresse (GeoMapFish-Permalink `map_x/map_y/map_zoom`, nur aus dem Aufbau abgeleitet, nicht getestet).
- `NE_Neuchâtel_Anleitung.txt`:
  - **Weg A:** SITN sitn.ne.ch/theme/cadastre, gratis, ohne Login, Captcha je Abfrage. Kaito fragt einzeln ab.
  - **Weg B:** Mailentwurf auf Französisch an den Registre foncier (SGRF), Rue de Tivoli 22, Case postale 1, 2002 Neuchâtel 2, 032 889 67 50, registrefoncier@ne.ch, **verifiziert** auf ne.ch. Nichts versendet.
- kantone_quellen.md: NE-Zeile um Direktlink-Muster und verifizierten SGRF-Kontakt ergänzt.

## Probleme
- OSM deckt Neuchâtel lückenhaft ab (30 von 120 Adressen fehlten). Die EXTRA-Punkte stammen aus den amtlichen Koordinaten (LV95 nach WGS84 mit der swisstopo-Näherungsformel umgerechnet, Genauigkeit etwa 1 m).
- OSM-Adresse «Rue Saint-Maurice 0» (be-BOP) ist vermutlich ein Erfassungsfehler, sie liegt auf derselben Parzelle wie Nr. 9. Nur vermerkt.
- Ein Key «rue du seyon» (kleingeschrieben in OSM, 1 Adresse) wird von der Karte nicht erfasst, nicht ergänzt.
- Kein Grundbuch- oder Eigentümerportal wurde abgefragt. Von SITN wurde nur die Startseite gelesen. Fremde untracked Dateien wurden nicht committet.
