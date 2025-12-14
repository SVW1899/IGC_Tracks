## Modul, zur Kommunikation mit dem Betriebssystem
import os

## Einfügen der IGC-Track Datei
DATEINAME = "data/0A4G3HI5.IGC"

## Kontrolle, ob die Datei existiert
if os.path.exists(DATEINAME):
    print (DATEINAME + " gefunden")

    ## Datei öffnen und Zeilen einlesen; with open schließt die Datei automatisch wieder, 'r' steht für 'read'
    with open(DATEINAME, "r") as datei:
        inhalt = datei.readlines()

    ## Bestimmung der Anzahl der Zeilen in der Datei
    anzahl_zeilen = len(inhalt)
    print("Die Datei hat", anzahl_zeilen, "Zeilen.")

    ## Ausgabe der ersten 5 Zeilen der Datei
    print("\nDie ersten 5 Zeilen der Datei:")
    for zeile in inhalt[:5]:
        print(zeile.strip())  # .strip() entfernt überflüssige Leerzeichen und Zeilenumbrüche

else:
    print (DATEINAME + " nicht gefunden")

## Liste für B-Records initialisieren
b_records = []

## Durchlaufen aller Zeilen in der Datei und Extrahieren der B-Records
for zeile in inhalt:
    if zeile.startswith('B'):
        b_records.append(zeile.strip()) # .strip() entfernt überflüssige Leerzeichen und Zeilenumbrüche

## Ausgabe der Anzahl der gefundenen B-Records
print("Es wurden",len(b_records),"B-Records gefunden.")

## Testausgabe der ersten 3 B-Records
if len(b_records) >= 3:
    print("Die ersten 3 B-Records:", b_records[:3])