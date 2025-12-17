## Modul, zur Kommunikation mit dem Betriebssystem
from igc_lib import *

## 1. Einfügen der IGC-Track Datei
DATEINAME = "data/0A4G3HI5.IGC"

## 2. Einlesen und Aufbereitung der IGC-Datei
parsed_data = parse_b_record(DATEINAME)

## 3. Erstellen eines DataFrames aus den aufbereiteten Daten
dataframe = create_dataframe(parsed_data)

## 4. Ausgabe des Plots
plot = plot_height_over_time(dataframe)



       