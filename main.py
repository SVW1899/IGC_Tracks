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
