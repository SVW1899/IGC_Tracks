## Modul, zur Kommunikation mit dem Betriebssystem
import os

## Einfügen der IGC-Track Datei
DATEINAME = "data/0A4G3HI5.IGC"

# 1. Wo steht Python gerade? (Current Working Directory)
aktueller_ort = os.getcwd()
print("Ich befinde mich hier:", aktueller_ort)

# 2. Was sieht Python in diesem Ordner?
print("Hier sehe ich folgende Dateien/Ordner:")
print(os.listdir(aktueller_ort))

# 3. Falls der Ordner 'data' existiert, schauen wir da mal rein
if "data" in os.listdir(aktueller_ort):
    print("\nIm Ordner 'data' sehe ich:")
    print(os.listdir("data"))
else:
    print("\nIch sehe keinen Ordner namens 'data' hier.")