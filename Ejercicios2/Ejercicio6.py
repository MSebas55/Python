import hashlib
import json


def main():
    usuarios = cargarusuarios()

    while True:
        print("\n--- Menú ---")
        print("1. Registrarme")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrarusuario(usuarios)
        elif opcion == "2":
            iniciosesion(usuarios)
        elif opcion == "3":
            guardarusuarios(usuarios)
            print("Fin del programa")
            break
        else:
            print("Introduce una opción válida")


def registrarusuario(usuarios):
    nombre = input("Nombre de usuario: ")

    if nombre in usuarios:
        print("El usuario ya existe.")
        return

    password = input("Contraseña: ")
    hash_pass = hashlib.sha256(password.encode()).hexdigest()

    usuarios[nombre] = hash_pass
    print("Usuario registrado con éxito.")
    # print(usuarios)


def guardarusuarios(usuarios):
    with open("usuarios.json", "w") as file:
        json.dump(usuarios, file)


def cargarusuarios():
    try:
        with open("usuarios.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def iniciosesion(usuarios):
    nombre = input("Nombre de usuario: ")
    if nombre not in usuarios:
        print("El usuario no existe, regístrese primero")
        return

    hash_pass_guardada = usuarios[nombre]

    password = input("Contraseña: ")
    hash_pass_ingresada = hashlib.sha256(password.encode()).hexdigest()

    if hash_pass_guardada == hash_pass_ingresada:
        print("Bienvenido")
        return
    else:
        print(f"Contraseña incorrecta.")


main()
