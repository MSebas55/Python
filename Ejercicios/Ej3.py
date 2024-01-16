# Obtener la representación inversa de una cadena de caracteres introducida por el usuario (sin usar arrays)
cadena = input("Introduce una cadena:")
cadenaInversa = ""

for i in range(len(cadena)-1, -1, -1):
    cadenaInversa += cadena[i]
print(cadenaInversa)