## Importieren der benötigten Module
import os ## Modul, zur Kommunikation mit dem Betriebssystem
import pandas as pd ## Modul zur Arbeit mit Dataframes
import datetime as dt ## Modul zur Arbeit mit Datum und Zeit
import matplotlib.pyplot as plt ## Modul zur Erstellung von Diagrammen
import geopandas as gpd ## Modul zur Erzeugung von Geometrien 
import webbrowser as wb ## Modul, um erzeugte HTML-Datei im Browser zu öffnen
from shapely import LineString ## Modul zur Erstellung eines LineStrings aus Koordinaten

## Funktion zur Umwandlung von Koordinaten im DMS-Format in das DD-Format
def convert_into_DD(coordinate_str, is_lat_str=True):

    direction = coordinate_str[-1] # Letztes Zeichen der Koordinate (N, S, E, W)
    value = coordinate_str[:-1] # Koordinatenwert ohne Richtungsangabe

    ## Umwandlung des Breitengrades (DDMMmmm)
    if is_lat_str == True:
        lat_DD = int(value[0:2]) 
        lat_MM = int(value[2:4])
        lat_mmmm = int(value[4:7])
        coord_DD = lat_DD + (lat_MM / 60) + (lat_mmmm / 1000 / 60)

    ## Umwandlung des Längengrades (DDDMMmmm)
    else:
        lon_DDD = int(value[0:3])
        lon_MM = int(value[3:5])
        lon_mmmm = int(value[5:8])
        coord_DD = lon_DDD + (lon_MM / 60) + (lon_mmmm / 1000 / 60)
    
    ## Anpassung des Vorzeichens je nach Himmelsrichtung
    if direction in ['S', 'W']:
        coord_DD = coord_DD * (-1)
    
    return coord_DD

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
            timeHH = clean_zeile[1:3]
            timeMM = clean_zeile[3:5]
            timeSS = clean_zeile[5:7]
            lat_str = clean_zeile[7:15]
            lon_str = clean_zeile[15:24]
            alt_baro_str = clean_zeile[25:30] ## Barometrische Höhe
            alt_gps_str = clean_zeile[30:35] ## GPS-Höhe

            ## Speichern der einzelnen extrahierten B-Records in ein Dictionary
            daten_punkt = {
                "time": dt.time(int(timeHH), int(timeMM), int(timeSS)), #Umwandlung der Zeitangaben in timestamp
                "lat": convert_into_DD(lat_str, True), #Umwandlung Breitengrad DMS in DD
                "lon": convert_into_DD(lon_str, False), #Umwandlung Längengrad DMS in DD
                "alt_baro": int(alt_baro_str), #Umwandlung der barometrischen Höhe in einen Integer
                "alt_gps": int(alt_gps_str)    #Umwandlung der GPS-Höhe in einen Integer
            }
       
            ## Speichern des Dictionaries in die Daten_Liste
            data_list.append(daten_punkt)

    ## Test
    print("Es wurden", len(data_list), "Datenpunkte extrahiert")
    if len(data_list) > 1:
        print("Beispieldatenpunkt 1:", data_list[0])
    
    ## Rückgabe der aufbereiteten Datenliste
    return data_list

## Funktion zum Erstellen eines DataFrames aus den aufbereiteten Daten
def create_dataframe(parsed_data):
    df = pd.DataFrame(parsed_data)
    print("DataFrame erstellt mit", len(df), "Einträgen.")
    print(df.head())  ## Ausgabe der ersten Zeilen des DataFrames
    print("\nDatentypen der Spalten:")
    print(df.info())  ## Ausgabe der Informationen zum DataFrame
    return df

## Funktion zum Plotten der Höhe über der Zeit
def plot_height_over_time(df):
    df.plot(x='time', y='alt_baro', title='Höhenprofil barometrische Höhe', xlabel='Zeit', ylabel='barometrische Höhe (m)')
    plt.show()
    return plt

## Funktion zum Erstellen eines GeoDataFrames aus dem DataFrame
def creating_geodataframe(df):

    ## Umwandeln der Koordinaten in Geometrien
    geometry = gpd.points_from_xy(df['lon'], df['lat'])
    

    ## Erstellen eines GeoDataFrames
    gdf = gpd.GeoDataFrame(
        df, geometry=geometry, crs="EPSG:4326")
    return gdf

## Funktion zum Testen der geometrischen Richtigkeit der aufgenommenen Punkte
def test_plot_points (gdf):
    gdf.plot(legend=True, markersize=0.5)
    plt.title('Testplot zur Überprüfung der geometrischen Richtigkeit der aufgenommenen Punkte')
    plt.xlabel('Längengrad')
    plt.ylabel('Breitengrad')
    plotted_route = plt.show()
    return plotted_route

## Funktion zum Erstellen einer interaktiven Webkarte
def create_map(gdf, DATEINAME):
    
    
    
    map = gdf.explore()

    #Speichern als Datei
    filename = DATEINAME + "_map.html"
    map.save(filename)
    print("Karte gespeichert als:", filename)
    
    #Automatisches Öffnen der HTML-Datei im Browser
    wb.open('file://' + os.path.realpath(filename))

    return map