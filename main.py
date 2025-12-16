## Modul, zur Kommunikation mit dem Betriebssystem
from igc_lib import *

## 1. Einfügen der IGC-Track Datei
DATEINAME = "data/0A4G3HI5.IGC"

## 2. Einlesen und Aufbereitung der IGC-Datei
parsed_data = parse_b_record(DATEINAME)

## 3. Erstellen eines DataFrames aus den aufbereiteten Daten
dataframe = create_dataframe(parsed_data)
print("DataFrame erstellt mit", len(dataframe), "Einträgen.")
print(dataframe.head())  ## Ausgabe der ersten Zeilen des DataFrames
print("\nDatentypen der Spalten:")
print(dataframe.info())  ## Ausgabe der Informationen zum DataFrame



       