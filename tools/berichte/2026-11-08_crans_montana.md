# Crans-Montana (VS), Lauf 08.11.2026

## Strassen
Bestätigt (strassen_ok): Rue Centrale, Route du Rawyl, Rue du Prado, Route de la Moubra, Rue du Pas-de-l'Ours (alle bisher in CITIES). Neu ergänzt: **Rue du Grand-Place** (Crans-Kern, Investis), **Rue Louis Antille**, **Avenue de la Gare** und **Place du Marché** (Montana-Kern, fehlte bisher ganz) sowie die OSM-Schreibweisen Rue du Pas de l'Ours und Rue Louis-Antille. Das sind mehr als die üblichen 4 bis 5 Strassen, weil Crans und Montana zwei getrennte Zentren sind.

- Rue du Pas de l'Ours ist auf den Kern bis Nr. 7 gekürzt, Route de la Moubra auf Nr. 1 bis 12 und 15. Weiter draussen liegen Wohnen und Hotels.
- Kandidat für später: Route de Vermala (Zermatten Sports, Boulangerie Gerber), Rue Théodore Stéphani (ALDI, 3 Adressen).

## Gemeindegrenze Lens (wichtig)
Rue du Prado (ausser Nr. 1), Rue du Grand-Place, eine Adresse an der Rue Centrale und Teile der Rue du Pas de l'Ours liegen amtlich in der **Gemeinde Lens**, nicht in Crans-Montana (swissBOUNDARIES3D, aktueller Jahrgang). Das betrifft 38 Adressen. Die Karte lädt nur die OSM-Gemeinde Crans-Montana, deshalb stehen sie jetzt in `EXTRA['Crans-Montana']`, mit OSM-Position. Im Tooltip erscheint dort der feste Text «keine OSM-Adresse», obwohl die Adressen in OSM vorhanden sind.

Bestehender Fehler, nicht überschrieben: Rue du Prado 19 steht als `parcel` «Crans-Montana 715», amtlich ist es **Lens 715** (E-GRID CH773043075259 in notes stimmt).

## Adressen
192 SEED-Einträge: Route du Rawyl 45, Rue Centrale 44, Rue du Prado 28, Avenue de la Gare 25, Rue Louis Antille 13, Route de la Moubra 13, Rue du Pas de l'Ours 8, Rue du Grand-Place 6, Place du Marché 5, Rue du Pas-de-l'Ours 3, Rue Louis-Antille 2.

Vier Adressen sind wegen der zwei OSM-Schreibweisen doppelt angelegt (Rue du Pas de l'Ours 1a/1b, Rue Louis Antille 1/3), damit auf der Karte beide Punkte Daten zeigen. Eindeutig sind es also 188 Adressen.

## Mieter
88 Adressen mit Mieter, davon 87 neu (122 Mieter, OSM, nicht vor Ort geprüft). 63 Adressen stammen ganz oder teilweise aus der Gebäude-Zuordnung von Läden ohne OSM-Adresse. Bei Gebäuden mit mehreren Adressen ist die nächstgelegene genommen und das in notes vermerkt (u.a. Moncler Prado 6, Julius Baer Prado 4). Edelweiss Market («Rue de Grand Palace 6» in OSM, Tippfehler) und Benetton («Rue du Grand Place 14») sind auf die amtlichen Rue-du-Grand-Place-Adressen gelegt. Die Brand-Sammelliste an Place du Marché 5 wurde durch den Ladennamen Avalanche Pro Shop ersetzt.

POIs ohne passendes Gebäude oder ausserhalb der gewählten Strassen blieben unzugeordnet, darunter Coop und Denner in Montana (andere Strassen).

## Eigentümer
Der Register-Abgleich lief einmal, nach dem Eintragen der Mieter. Neu: **Rue du Grand-Place 12 und 14 = Investis Holding SA** (Annual Report 2025, S. 110 bis 111, dort «Grand Place 12/14», Alleineigentum; Parzelle Lens 578). Bestätigt: Route du Rawyl 10, Rue du Prado 19. UID CHE-137.077.813 und Sitz bei allen vier ergänzt.

Stand: 4 von 192 mit Eigentümer, **188 offen**. Rue du Grand-Place 10 liegt auf derselben Parzelle 578 und ist nur als «vermutlich Investis, ungeprüft» in notes vermerkt. Parzelle und E-GRID sind bei allen gesetzt. Rue du Pas de l'Ours 6, Rue du Prado 2, 3, 6, Avenue de la Gare 16 fehlen im amtlichen Verzeichnis, Parzelle per OSM-Punkt.

Der Abgleich trug nebenbei 2 neue Eigentümer in anderen Städten ein (Buchs SG, Winterthur) und 2 Hinweise (St. Gallen, Zug). Dazu Konflikte in anderen Städten: 5, unverändert.

## Anfrageliste
`~/Downloads/Retail Map Anfragen/VS_Crans_Montana.csv` (161 Parzellen, 183 Adressen, Prio 1: 20, Prio 2: 89, Prio 3: 52; Spalte Gemeinde) und `VS_Crans_Montana_Anleitung.txt` mit Portalhinweisen und fertiger Mail auf Französisch. Nichts versendet.

- Crans-Montana (128 Parzellen): online.vs.ch, Login, 10 pro Tag (geteilt mit Sion und Zermatt), online «oui».
- Lens (33 Parzellen, darunter die Luxuslagen Rue du Prado 10, 12, 18 u.a.): laut amtlicher Liste **nicht online**, nur Grundbuchamt Siders.
- Grundbuchamt Siders, Av. du Marché 5, 3960 Sierre, 027 607 80 40, RF-Sierre@admin.vs.ch: verifiziert auf vs.ch/de/web/srf/contacts, Zuständigkeit aus der Liste «Online verfügbare Gemeinden» (19.09.2025). In `kantone_quellen.md` nachgetragen.

## Probleme
- Sektoren der fusionierten Gemeinde: Ob das Portal für Crans-Montana Sektoren verlangt, ist nicht geprüft. In der Spalte Hinweis steht die frühere Gemeinde nach historischer Grenze, das E-GRID ist massgeblich.
- Keine Antworten von Kaito vorhanden (`Antworten/` existiert nicht).
- Keine Portalabfragen, keine Logins, keine Mails.
