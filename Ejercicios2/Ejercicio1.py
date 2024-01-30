# Leer el contenido de una carpeta diferenciando entre ficheros y directorios.
import os
ruta = r'D:\Github Desktop\Python\Ejercicios2'
print(f"Ruta: {ruta}")
ejecutables_escritorio = os.listdir(ruta)
# print(ejecutables_escritorio)
archivos = []
directorios = []
for f in ejecutables_escritorio:
    nombre_archivo = os.path.join(ruta, f)
    if os.path.isfile(nombre_archivo):
        archivos.append(f)
    elif os.path.isdir(nombre_archivo):
        directorios.append(f)
    else:
        print("Rareza")
print(f"Archivos: {archivos}")
print(f"Directorios: {directorios}")
