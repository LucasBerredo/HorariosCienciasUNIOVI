# HorariosCienciasUNIOVI
Convierte los horarios de la Facultad de Ciencias de UniOvi para el curso 23/24 de Excel a ICS (calendario)

## Uso:
Ejecuta el script de Python
Vas a necesitar la siguiente estructura:

    Escritorio
    ↳ archivosCSV
      ↳ dias
    ↳ archivosICS
    ↳ HorariosICS.py
    ↳ (tuHorario).csv

NOTA: No tiene por qué ejecutarse en el escritorio, siempre que la estructura relativa siga igual

Para conseguir el archivo .csv:

1. Abre Excel, exporta como .csv
2. Abre el .csv con un **editor de texto** y borra las primeras líneas (lo primero debería ser "2º Semestre Semana 1;"

En la carpeta "archivosICS", el script generará un archivo .ics para cada hora. Se pueden abrir con la mayoría de aplicaciones de calendario.


## Requisitos
- Python 3.11+
- Windows/MacOS/Linux/una patata que corra Python
