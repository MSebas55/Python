import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

while True:
    # Pedir al usuario que ingrese un número
    intento = int(input("Adivina el número entre 1 y 100: "))

    # Comprobar si el número es el correcto
    if intento == numero_secreto:
        print("¡Adivinaste! ¡Ese era el número secreto!")
        break
    elif intento < numero_secreto:
        print("Intenta con un número más grande.")
    else:
        print("Intenta con un número más pequeño.")
