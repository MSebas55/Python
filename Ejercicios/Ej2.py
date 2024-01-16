from datetime import datetime

# Obtener la fecha actual
fecha_actual = datetime.now()

# Pedir al usuario que introduzca una fecha
fecha_ingresada_str = input("Introduce una fecha en formato DD/MM/YYYY: ")

# Convertir la cadena de fecha ingresada a un objeto datetime
fecha_ingresada = datetime.strptime(fecha_ingresada_str, "%d/%m/%Y")

# Calcular la diferencia en días
diferencia_en_dias = (fecha_actual - fecha_ingresada).days

# Mostrar el resultado
print(f"La diferencia en días entre {fecha_ingresada_str} y hoy es: {diferencia_en_dias} días.")