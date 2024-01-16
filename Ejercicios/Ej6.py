import os

# Pedir al usuario que introduzca la ruta del archivo
ruta_archivo = input("Introduce la ruta del archivo: ")

# Obtener la extensión del archivo
nombre_archivo, extension = os.path.splitext(ruta_archivo)

# Mostrar el resultado
print(f"El archivo '{nombre_archivo}' tiene la extensión '{extension[1:]}'")
