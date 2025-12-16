## Importieren der benötigten Module
import os ## Modul, zur Kommunikation mit dem Betriebssystem
#import pandas as pd ## Modul zur Arbeit mit Dataframes

## Funktion zum Einlesen und Aufbereiten der B-Records aus der IGC-Datei
def parse_b_record(DATEINAME):
    
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

    ## Liste für aufbereitete Daten
    data_list = []

    for zeile in inhalt:
        if zeile.startswith('B'):
            clean_zeile = zeile.strip()

            ## Extahieren der Werte aus dem B-Record 
            time = clean_zeile[1:7]
            lat_str = clean_zeile[7:15]
            lon_str = clean_zeile[15:24]
            alt_baro_str = clean_zeile[25:30] ## Barometrische Höhe
            alt_gps_str = clean_zeile[30:35] ## GPS-Höhe

            ## Speichern der einzelnen extrahierten B-Records in ein Dictionary
            daten_punkt = {
                "time": time,
                "lat": lat_str,
                "lon": lon_str,
                "alt_baro": alt_baro_str,
                "alt_gps": alt_gps_str
            }
       
            ## Speichern des Dictionaries in die Daten_Liste
            data_list.append(daten_punkt)

    ## Test
    print("Es wurden", len(data_list), "Datenpunkte extrahiert")
    if len(data_list) > 1:
        print("Beispieldatenpunkt 1:", data_list[0])
    
    ## Rückgabe der aufbereiteten Datenliste
    return data_list