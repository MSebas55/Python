"""
Jugar al 21.
Se trata de que un jugador comience una partida contra la casa. Se reparten 2 cartas a cada participante.
La casa mostrará siempre todas sus cartas menos la última.
El jugador puede seguir pidiendo cartas hasta que se pase de 21, momento en el que pierde, o decida plantarse.
Si decide plantarse, la casa se repartirá a sí misma hasta que el valor de sus cartas supere el número 16.
Si la casa no se ha pasado de 21, momento en el que el jugador gana, se comparan los resultados.
Aquel que se acerque más a 21 gana la partida. Se puede empatar.
"""

import random
class Carta:

    def __init__(self, nombre, palo, valor):
        self.nombre = nombre
        self.palo = palo
        self.valor = valor

    def __str__(self):
        return f"{self.nombre}"


baraja = []
casa = []
palos = ["oros", "copas", "espadas", "bastos"]

for palo in palos:
    for n in range(1, 11):
        if n == 1:
            baraja.append(Carta(f"As de {palo}", palo, 1))
        elif n == 8:
            baraja.append(Carta(f"Sota de {palo}", palo, 10))
        elif n == 9:
            baraja.append(Carta(f"Caballo de {palo}", palo, 10))
        elif n == 10:
            baraja.append(Carta(f"Rey de {palo}", palo, 10))
        else:
            baraja.append(Carta(f"{n} de {palo}", palo, n))
random.shuffle(baraja)
for carta in baraja:
    print(carta)


for i in range(1,3):
    sacada = random.randint(1, 11)
    casa.append(Carta(f"{sacada} de {palo}", palo[random.randint(1, len(palo))], sacada))
for carta in casa:
    print(carta)