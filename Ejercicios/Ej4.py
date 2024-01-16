# Pedir al usuario que introduzca números separados por comas
entrada_usuario = input("Introduce números separados por comas: ")

# Dividir la entrada en una lista utilizando la coma como delimitador
numeros_lista = [int(numero) for numero in entrada_usuario.split(',')]

# Mostrar la lista resultante
print("Lista de números:", numeros_lista)
