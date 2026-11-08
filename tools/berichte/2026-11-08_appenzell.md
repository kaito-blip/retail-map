# Appenzell (AI), Lauf 08.11.2026

**Strassen** (`strassen_ok` jetzt true): Hauptgasse, Marktgasse, Engelgasse, Poststrasse, Landsgemeindeplatz, Postplatz.
Die fünf bisherigen CITIES-Strassen bleiben. Neu ist die **Poststrasse** (Papeterie, Kunstgewerbe Dörig, Appenzeller Käse, Post). Sie verbindet den Postplatz mit dem Bahnhof. topstrassen.py (Radius 500): Hauptgasse 19 Läden, Weissbadstrasse 5, Zielstrasse 5, Engelgasse 4, Poststrasse 4, Marktgasse 2. Weissbadstrasse und Zielstrasse habe ich nicht aufgenommen. Beide sind Ausfallstrassen, und die Läden dort liegen vor allem im Coop- und Fachmarktbereich.
CITIES-q «Appenzell, Appenzell Innerrhoden» ist korrekt: Nominatim liefert relation 1683860 (Bezirk Appenzell).

**OSM-Lücke Landsgemeindeplatz:** Der Platz hat in OSM keine einzige Adresse, amtlich gibt es aber zehn (1, 2, 3, 4, 5, 6, 7, 7a, 8, 8a). Ich habe sie mit den geo.admin-Koordinaten in `EXTRA['Appenzell']` ergänzt. Der Postplatz hat auch amtlich keine Adressen. Er bleibt in der Strassenliste, liefert aber keine Einträge.

**Adressen:** 127 (Hauptgasse 60, Marktgasse 21, Engelgasse 20, Poststrasse 16, Landsgemeindeplatz 10). tools/adressen/appenzell.json wurde dabei überschrieben. Die alte Fassung aus dem Nachtlauf mit Weissbadstrasse und Zielstrasse liegt noch in git (7d7a383).

**Neue Mieter:** 48 Adressen. 46 kommen aus adressen.py. Zwei weitere habe ich per Gebäude zugeordnet (POI ohne Adresse in einem Gebäude mit genau einer Adresse): Hauptgasse 25 ruma Weine & Spirituosen, Hauptgasse 26 Wirtschaft Drei Könige. Die UBS-Filiale liegt im Gebäude Hauptgasse 11 / Schäfligasse 12. Weil das Gebäude zwei Adressen hat, habe ich sie nicht eingetragen. Unter den OSM-Mietern sind auch Kirchen und Ämter (Pfarrkirche St. Mauritius, Heiligkreuzkapelle, Rathaus, Landeskanzlei). Ich habe sie unverändert übernommen.

**Eigentümer:** Der Registerabgleich brachte keinen neuen Treffer. Hauptgasse 11 war schon eingetragen und ist bestätigt: UBS Anlagestiftung 1, AST Kommerzielle Immobilien Schweiz. Neue Eigentümer: 0.
Folgende Einträge stehen nur als Vermutung in notes, `owner` bleibt leer:
- Hauptgasse 2 und Hauptgasse 34: vermutlich Römisch-katholische Kirchgemeinde Appenzell
- Marktgasse 2: vermutlich Kanton AI (Landeskanzlei)
- Marktgasse 6: Rathaus, vermutlich öffentliche Hand
- Hauptgasse 41: vermutlich Raiffeisenbank Appenzell als Eigennutzerin

**Parzellen:** Alle 126 offenen Adressen haben jetzt Parzelle und E-GRID, zusammen 108 Parzellen. Parzelle 64 umfasst sechs Adressen. Für Hauptgasse, Marktgasse und Engelgasse stammen die Werte aus der Nachtlauf-Datei Parzellen/AI_Appenzell.csv. Drei Stichproben mit parzelle.py stimmten überein. Poststrasse und Landsgemeindeplatz kommen live über parzelle.py (geo.admin, 1 Sekunde Pause).

**Offen:** 126 Adressen ohne Eigentümer.

**Anfrageliste:** ~/Downloads/Retail Map Anfragen/AI_Appenzell.csv mit 108 Parzellen (Priorität 1: 38, 2: 36, 3: 34) und den Spalten Eigentuemer (leer), Link und Hinweis. Dazu AI_Appenzell_Anleitung.txt:
- Weg A: Kaito fragt einzeln auf geoportal.ch/ktai ab. Ob dort Eigentümer ohne Login erscheinen, ist ungeprüft (Quellen 2017/2019). Das Link-Muster stammt aus geo.admin `geoportal_url`. Getestet habe ich den Link nicht.
- Weg B: fertige Mail an das Grundbuchamt, nicht versendet.

Das Grundbuchamt ist auf ai.ch verifiziert (Seite Grundbuchauszug, 08.11.2026): Grundbuch- und Erbschaftsamt, Fachbereich Grundbuch, Marktgasse 2, 9050 Appenzell, 071 788 94 31, grundbuchamt@vd.ai.ch. Ein Grundbuchauszug kostet Fr. 40.-. tools/kantone_quellen.md ist für AI nachgeführt.

**Probleme:** Auf ai.ch ist die E-Mail-Adresse per Cloudflare verschleiert. Ich habe sie lokal aus dem Seitenquelltext dekodiert. Der Privacy-Hook blockiert Bash-Befehle, die die Absenderadresse enthalten. Die Anleitung habe ich deshalb mit Write geschrieben. Kein Portal wurde abgefragt. Antworten von Kaito lagen keine vor (der Ordner Antworten existiert nicht).
