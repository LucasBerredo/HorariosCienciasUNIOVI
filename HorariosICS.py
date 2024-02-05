# Horarios CSV - Pasa el horario de la Facultad de Ciencias a ICS para añadir a la app del calendario
# Lucas Berredo de la Colina - 21/01/24
# Por favor no juzgues mucho el código, fue un proyecto de una tarde


# Importar módulos
import csv
from secrets import token_hex
import re
from datetime import datetime, timedelta


# Comandos Regex
expresion1 = "[1,2]...."
p = re.compile(expresion1)
expresion2 = "-[1,2]...."
q = re.compile(expresion2)
expresion3 = "^((.*?,)([^',]*)){2}.*"
r = re.compile(expresion3)
expresion4 = "[1-9]', '(.*)\']"
s = re.compile(expresion4)


horasPorDia = [6,6,6,3,0,6,6,6,4,5,6,6,7,4,5,7,6,7,5,6,6,6,6,4,5,6,6,7,4,6,6,6,5,4,6,7,6,7,4,5,6,6,7,5,5,0,0,0,0,0,7,6,6,5,6,6,6,6,3,5,6,6,6,5,5,6,6,7,4,5,7,6,0,5,7]


# Función - Admite un csv y crea un archivo por cada evento
def createFileFromCSV(j,k):
    with open("archivosCSV/"+str(5*j+k)+".csv", newline='') as csvfile:
        day = str(datetime(2024,1,21) + timedelta(days=(7*j+k)))
        day = day[0:4] + day[5:7] + day[8:10]
        day = str(int(day)+1)
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in reader:
            fechainicio = (p.search(str(row))).group(0)
            fechainicio = day+"T"+fechainicio[0:2]+fechainicio[3:5]+"00"
            fechafin = (q.search(str(row))).group(0)
            fechafin = day+"T"+fechafin[1:3]+fechafin[4:6]+"00"
            nombreEvento = (r.search(str(row))).group(2)
            nombreEvento = nombreEvento[1:len(nombreEvento)-2]
            aula = (s.search(str(row))).group(1)
            uid = ("UID:"+str(token_hex(4))+"-"+str(token_hex(2))+"-"+str(token_hex(2))+"-"+str(token_hex(2))+"-"+str(token_hex(6))).upper()

            archivo = "archivosICS/"+fechainicio+nombreEvento+".ics"
            f = open(archivo, "+a")
            f.write("BEGIN:VCALENDAR\n")
            f.write("CALSCALE:GREGORIAN\n")
            f.write("VERSION:2.0\n")
            f.write("X-WR-CALNAME:"+str(nombreEvento)+"\n")
            f.write("METHOD:PUBLISH\n")
            f.write("PRODID:lucasberredo\n")
            f.write("BEGIN:VTIMEZONE\n")
            f.write("TZID:Europe/Madrid\n")
            f.write("BEGIN:DAYLIGHT\n")
            f.write("TZOFFSETFROM:+0100\n")
            f.write("RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU\n")
            f.write("DTSTART:19810329T020000\n")
            f.write("TZNAME:CEST\n")
            f.write("TZOFFSETTO:+0200\n")
            f.write("END:DAYLIGHT\n")
            f.write("BEGIN:STANDARD\n")
            f.write("TZOFFSETFROM:+0200\n")
            f.write("RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU\n")
            f.write("DTSTART:19961027T030000\n")
            f.write("TZNAME:CET\n")
            f.write("TZOFFSETTO:+0100\n")
            f.write("END:STANDARD\n")
            f.write("END:VTIMEZONE\n")
            f.write("BEGIN:VEVENT\n")
            f.write(uid+"\n")
            f.write("TRANSP:OPAQUE"+"\n")
            f.write("CREATED:20240121T150000Z\n")
            f.write("DTEND;TZID=Europe/Madrid:"+str(fechafin)+"\n")
            f.write("SUMMARY:"+str(nombreEvento)+"\n")
            f.write("LOCATION:"+str(aula)+"\n")
            f.write("LAST-MODIFIED:20240121T150000Z\n")
            f.write("DTSTAMP:20240121T150000Z\n")
            f.write("DTSTART;TZID=Europe/Madrid:"+str(fechainicio)+"\n")
            f.write("SEQUENCE:0\n")
            f.write("END:VEVENT\n")
            f.write("END:VCALENDAR\n")
            f.close()

# Introduccion
print("  _    _                           _               _____   _____ __      __")
print(" | |  | |                         (_)             / ____| / ____|\ \    / /")
print(" | |__| |  ___   _ __  __ _  _ __  _   ___   ___ | |     | (___   \ \  / / ")
print(" |  __  | / _ \ | '__|/ _` || '__|| | / _ \ / __|| |      \___ \   \ \/ /  ")
print(" | |  | || (_) || |  | (_| || |   | || (_) |\__ \| |____  ____) |   \  /   ")
print(" |_|  |_| \___/ |_|   \__,_||_|   |_| \___/ |___/ \_____||_____/     \/    ")
print("Hecho por Lucas Berredo")
print("\n")
print("INSTRUCCIONES")
print("1.- GUARDA EL EXCEL CON TUS HORARIOS COMO .CSV")
print("2.- QUITA LAS PRIMERAS LÍNEAS DEL ARCHIVO - LO PRIMERO DEBE SER 2º SEMESTRE SEMANA 1")
print("3.- CREA LAS CARPETAS \"archivosCSV\", \"archivosICS\" y \"dias\" (dentro de archivosCSV)")
archivoCSV = input("4.- ESCRIBE EL NOMBRE DE TU ARCHIVO AQUÍ (INCLUYENDO .CSV) Y DALE AL ENTER")
print("5.- Y YA ESTÁ, TIENES TUS HORARIOS EN LA CARPETA archivosICS")




# Bucle - Crea los archivos CSV para cada día
lunes = open("archivosCSV/dias/lunes.csv","+w")
martes = open("archivosCSV/dias/martes.csv","+w")
miercoles = open("archivosCSV/dias/miercoles.csv","+w")
jueves = open("archivosCSV/dias/jueves.csv","+w")
viernes = open("archivosCSV/dias/viernes.csv","+w")

with open(archivoCSV, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=";", quotechar="|")
    for row in reader:
        if not ((re.match("\['2º",str(row)))):
            lunes.write(str(row[1])+";"+str(row[2])+";"+str(row[3])+"\n")
            martes.write(str(row[4])+";"+str(row[5])+";"+str(row[6])+"\n")
            miercoles.write(str(row[7])+";"+str(row[8])+";"+str(row[9])+"\n")
            jueves.write(str(row[10])+";"+str(row[11])+";"+str(row[12])+"\n")
            viernes.write(str(row[13])+";"+str(row[14])+";"+str(row[15])+"\n")

lunes.close()
martes.close()
miercoles.close()
jueves.close()
viernes.close()

lunes = open("archivosCSV/dias/lunes.csv","+r")
martes = open("archivosCSV/dias/martes.csv","+r")
miercoles = open("archivosCSV/dias/miercoles.csv","+r")
jueves = open("archivosCSV/dias/jueves.csv","+r")
viernes = open("archivosCSV/dias/viernes.csv","+r")
            
dias = [lunes, martes, miercoles, jueves, viernes]


for j in range(15):
    for k in range(len(dias)):
        archivoCSVdelimiter = str(j*5+k)+".csv"
        archivo = "archivosCSV/" + archivoCSVdelimiter
        f = open(archivo, "+a")

        for l in range(horasPorDia[j*5+k]):
            f.write(dias[k].readline())
        
        for l in range(11-horasPorDia[j*5+k]):
            dias[k].readline()

        f.close()
        createFileFromCSV(j,k)

lunes.close()
martes.close()
miercoles.close()
jueves.close()
viernes.close()


             
