import random


def valor_carta(carta):
    if carta in ['J', 'Q', 'K']:
        return 10
    elif carta == 'A':
        return 11
    else:
        return int(carta)


def repartir_carta():
    cartas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cartas)


def calcular_puntuacion(mano):
    return sum([valor_carta(carta) for carta in mano])


def mostrar_mano(mano):
    print(f"Mano de la casa: {', '.join(mano)}")

def mostrar_mano_jugador(mano):
    print(f"Tu mano: {', '.join(mano)}")
def jugar_21():
    # Inicialización
    mano_jugador = [repartir_carta(), repartir_carta()]
    mano_casa = [repartir_carta(), repartir_carta()]

    # Turno del jugador
    while True:
        print(f"Tu mano: {', '.join(mano_jugador)}")
        print(f"Tu puntuación: {calcular_puntuacion(mano_jugador)}")
        opcion = input("¿Quieres una carta más? (s/n): ").lower()

        if opcion == 's':
            mano_jugador.append(repartir_carta())
            if calcular_puntuacion(mano_jugador) > 21:
                print("Te has pasado de 21. ¡Has perdido!")
                return
        else:
            break

    # Turno de la casa
    while calcular_puntuacion(mano_casa) <= 16 or calcular_puntuacion(mano_casa) < calcular_puntuacion(mano_jugador):
        mano_casa.append(repartir_carta())

    # Mostrar las manos
    mostrar_mano_jugador(mano_jugador)
    mostrar_mano(mano_casa)

    # Determinar el ganador
    print("")
    puntuacion_jugador = calcular_puntuacion(mano_jugador)
    puntuacion_casa = calcular_puntuacion(mano_casa)
    print(f"Tu puntuación: {calcular_puntuacion(mano_jugador)}")
    print(f"Puntuación de la casa: {calcular_puntuacion(mano_casa)}")

    if puntuacion_casa > 21:
        print("La casa se ha pasado de 21. ¡Ganas!")
    elif puntuacion_jugador > puntuacion_casa:
        print("¡Ganas!")
    elif puntuacion_jugador < puntuacion_casa:
        print("La casa gana.")
    else:
        print("Empate.")


# Jugar al 21
jugar_21()