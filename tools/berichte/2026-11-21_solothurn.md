# Solothurn, Folgelauf 21.11.2026

Erster Lauf war am 08.11.2026. Heute nur Schritt 4 (Eigentümer) für die offenen Adressen.

- **Strassen** (unverändert): Hauptgasse, Gurzelngasse, Stalden, Marktplatz, Schmiedengasse
- **Adressen in der SEED:** 145, davon 3 mit Eigentümer (Hauptgasse 59 SPSS IF Commercial, Hauptgasse 64 Swiss Prime Anlagestiftung, Hauptgasse 70 Kanton Solothurn)
- **Neue Mieter:** 0 (kein neuer Adresslauf)
- **Neue Eigentümer:** 0
- **Offen:** 142. Alle haben schon Parzelle und E-GRID, eine weitere parzelle.py-Abfrage war nicht nötig.

## Register-Abgleich
`register_abgleich.py --schreiben`: 0 neu, für Solothurn 3 bestätigt. Der Lauf hat wieder die bekannten falschen UBS-Sima-Konflikthinweise an Luzern Grendelstrasse 15/19 (Ennetbaden) angehängt. Ich habe sie vor dem Commit zurückgesetzt (siehe Zug- und Luzern-Gotchas).

## Recherche in öffentlichen Quellen
- Hauptgasse 60 (Jesuitenkirche, Parzelle 3377): Die Regierungsratsbeschlüsse 2009/1072 und 2011/384 zahlen die Denkmalpflege-Beiträge an die Römisch-katholische Kirchgemeinde Solothurn, der RRB 2015/1431 an die Stiftung Jesuitenkirche Solothurn. Die Eigentümerschaft wird nirgends namentlich genannt. Der Hinweis steht in notes, `owner` bleibt leer.
- Hauptgasse 66 (St.-Ursen-Kathedrale, Parzelle 485): Laut RRB 2012/653 ist die Kirchgemeinde Bauherrin. In notes steht deshalb «vermutlich Römisch-katholische Kirchgemeinde Solothurn, ungeprüft».
- Pfarrhaus St. Ursen (Kirchgemeinde seit 1885) liegt an der Propsteigasse 10 und damit nicht an einer der erfassten Strassen.

## Anfragelisten
- `~/Downloads/Retail Map Anfragen/SO_Solothurn.csv` und `SO_Solothurn_Anleitung.txt` vom 08.11. gelten weiter: 136 Zeilen nach Priorität sortiert, mit Direktlinks auf geo.so.ch. Die Spalte Eigentuemer ist noch leer, Kaito hat also noch keine Abfragen eingetragen.
- Weg A ist die Online-Eigentümerabfrage auf geo.so.ch (gratis, einzeln). Weg B ist das Grundbuchamt Region Solothurn, gb.so@fd.so.ch (verifiziert 08.11.).

## Antworten
In `Antworten/` lagen keine neuen Dateien und keine `_nicht_zugeordnet_*.csv`.

## Probleme
Keine. Es wurden keine Portale abgefragt.
