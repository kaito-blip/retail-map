# Tageslauf 08.11.2026: Solothurn (SO)

## Strassen
Hauptgasse, Gurzelngasse, Stalden, Marktplatz, Schmiedengasse. `strassen_ok` steht jetzt auf true.
Ergebnis `topstrassen.py` (Radius 800 m): Hauptgasse 27 Läden, Stalden 17, Gurzelngasse 14, Rossmarktplatz 8, Schmiedengasse 6, Klosterplatz 6, Friedhofplatz 4, Bielstrasse 5, Hauptbahnhofstrasse 3.
- Hauptgasse: Hauptachse der Altstadt mit H&M, Interdiscount, Calida, Ochsner Shoes, Rituals, Beldona, Lego.
- Gurzelngasse: Fielmann, Läderach, Swisscom, Sunrise, McOptic, Bayard.
- Stalden: Fortsetzung der Hauptgasse Richtung Aare, viele Fachgeschäfte.
- Marktplatz: Zentrum mit Zytglogge, in OSM nur eine Adresse (Marktplatz 2).
- Schmiedengasse: neu, Querachse mit Schmuck- und Fachgeschäften, in CITIES ergänzt.
- Hauptbahnhofstrasse (nur 3 Läden, Bahnhofsquartier südlich der Aare) bleibt in CITIES, ist aber nicht mehr in staedte.json. CITIES-q «Solothurn, Bezirk Solothurn» ist eine OSM-Relation (1683577), unverändert.

## Zahlen
- **145 Adressen** aus OSM: Hauptgasse 68, Gurzelngasse 32, Stalden 25, Schmiedengasse 19, Marktplatz 1.
- **Neue Mieter:** 77 Adressen. Bei 1 Adresse stand schon ein Mieter.
- **Register-Abgleich:** 0 neue Eigentümer. Schon vorhanden: Hauptgasse 59 (SPSS Investment Fund Commercial), Hauptgasse 64 (Swiss Prime Anlagestiftung). Das Register hat für Solothurn sonst nur Adressen ausserhalb der gewählten Strassen (Rossmarktplatz 1 Ecoreal, Kronengasse 17 SPA, Hauptbahnhofstrasse PKSO ohne Nummer).
- **UID und Sitz aus Zefix:** Swiss Prime Site Solutions AG CHE-211.793.771 (Zug), Swiss Prime Anlagestiftung CHE-374.175.355 (Olten).
- **Hinweis in notes** (owner leer): Hauptgasse 60 (Jesuitenkirche) vermutlich Einwohnergemeinde Solothurn, ungeprüft. Keine weiteren Eigentümer aus öffentlichen Quellen belegbar.
- **Parzelle und E-GRID** für alle 143 offenen Adressen gesetzt (136 Parzellen). Marktplatz 2 ist nicht im amtlichen Adressverzeichnis; die Parzelle 727 wurde per OSM-Koordinate bestimmt und ist dieselbe wie Gurzelngasse 2.
- **Offen: 143 von 145 Solothurn-Einträgen.**
- **SEED:** 2641 Einträge, 614 mit Eigentümer. Gegen HEAD geprüft: kein Key verloren, kein bestehender Wert überschrieben.

## Anfrageliste
- `~/Downloads/Retail Map Anfragen/SO_Solothurn.csv`: 136 Parzellen, Spalten Prioritaet, Adresse, Parzelle, E-GRID, Mieter, Eigentuemer (leer), Link, Hinweis. Prio 1 = 51, Prio 2 = 65, Prio 3 = 20.
- `SO_Solothurn_Anleitung.txt`:
  - **Weg A:** Online-Eigentümerabfrage geo.so.ch/map/grundstuecksinformation, gratis, laut so.ch ohne Vorbedingungen, kein Limit genannt. Kaito fragt einzeln ab. Direktlinks zentriert auf das Gebäude (Muster `?c=E,N&s=500`, aus der Geoportal-Konfiguration `urlPositionFormat: centerAndZoom` abgeleitet; keine Abfrage abgesetzt).
  - **Weg B:** Mailentwurf an das Grundbuchamt Region Solothurn, Rötistrasse 4, 4502 Solothurn, gb.so@fd.so.ch, **verifiziert** auf so.ch. Eigentumsbescheinigung bis 10 Personen pro Tag gebührenfrei. Nichts versendet.

## Neue Erkenntnis
- SO ist kein reiner Bestell-Kanton: Es gibt eine freie Online-Eigentümerabfrage. kantone_quellen.md (Zeile SO und Kernergebnis) entsprechend korrigiert. Das gilt auch für Olten.

## Probleme
- Ein Datenschutz-Hook hat die Absender-Mailadresse in der Signatur der Anleitung blockiert. Platzhalter «[E-Mail ergänzen]», vor dem Versand ergänzen.
- Kein Grundbuch- oder Eigentümerportal wurde abgefragt. Fremde untracked Dateien wurden nicht committet.
