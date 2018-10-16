# wumbler-story
Das Ziel dieses Projekts ist es, einen Datensatz zu ’sammeln’ und zu beschreiben, allenfalls daraus eine zuverlässige Messmethode für das Wumbler Projekt zu erstellen. 

Damit das Ziel erreicht werden kann, werden mehrere Messungen der Bewegungen einer Waschmaschiene erstellt. Die Messdaten werden anschliessend aufbereitet und sollen eine Aussage über den 
Waschmaschienen Zustand wiedergeben. Dafür soll eine gute Messmethode mit aussagekräftige Resultaten gefunden werden.  


## Werkzeuge und Setup
Als Werkzeuge wird ein Raspberry PI Modell 3 und dem MPU-6050 Sensor verwendet.
Das Setup wurde mit der Anleitung: https://tutorials-raspberrypi.com/measuring-rotation-and-acceleration-raspberry-pi/ erstellt.
Nachfolgend eine kurze Beschreibung:

1. Raspberry PI Image Setup
2. Config der I2C Schnittstelle
3. Python Script um MPU-6050 Modul anzusprechen
4. Python Script für das Sammeln der Daten.

## Waschmaschiene
Schulthess Spirit topLine 8010
Zustand gebraucht, hat einige Jahre auf dem Bukel.
Siehe Bilder unter wumbler-story/img

## Messmethode
Das Raspberry pi wird an der Maschiene befestigt. Der MPU Sensor wird mit Klebeband an das 
Gehäuse der Waschmaschiene befestigt. Somit wird sichergestellt, dass z.B durch das Gehäuse 
keine Vibrationen abgefedert werden. 

Gemessen wurde 1 Minute vor dem Waschgang bei augeschlateter Waschmaschiene und bis ca. 1 Minute
nach dem Waschgang.

## Resultate
Die ersten Resultate sind in der Datei 2018-10-16-0.wd abgelegt.
Im Dateinamen steht das Datum der Datenerhebung.
Die Datei besteht aus zwei Header Zeilen und den Rohdaten.

Die Headers beschreiben die ID des Waschgangs und x, y, z die Sensordaten. Beispiel:

laundry: ce75f565-4b90-4421-9764-ae1304c4b6fb has started
x,y,z


Die x,y,z Dimensionen stehen für die Beschleunigung in die jeweilige Richtung. Für mehr Informationen siehe Datenblatt unter: https://www.invensense.com/wp-content/uploads/2015/02/MPU-6000-Datasheet1.pdf  
