# Obtener un conjunto de números separados por coma y crear una lista.

numerosuser = input("Introduce números separados por una coma: ")

listanum = [int(numero) for numero in numerosuser.split(',')]

print("Lista de números:", listanum)
