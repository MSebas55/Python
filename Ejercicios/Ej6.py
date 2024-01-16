# Obtener la extensión de un archivo especificado por el usuario.
import os
ruta = input("Introduce la ruta del archivo: ")

archivo = os.path.splitext(ruta)

print(f"El archivo '{ruta}' tiene la extensión {archivo[1:]}")
