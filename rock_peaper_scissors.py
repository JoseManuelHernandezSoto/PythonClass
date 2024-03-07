import random

def game(optionUser):
    # se crean las opciones de juego
    options = ["piedra", "papel", "tijeras"]
    # se elije una opcion al azar para la maquina
    optionsPC = random.choice(options)
    
    # Mostrar las opciones elegidas por el usuario y la computadora
    print("Tu elección:", optionUser)
    print("Elección de la computadora:", optionsPC)
    
    # Determinar el resultado del juego
    if optionUser == optionsPC:
        print("¡Empate!")
    elif (optionUser == "piedra" and optionsPC == "tijeras") or \
         (optionUser == "papel" and optionsPC == "piedra") or \
         (optionUser == "tijeras" and optionsPC == "papel"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

count = True
while count== True:
    # Pedir al usuario que elija entre piedra, papel o tijeras
    optionUser = input("Elige piedra, papel o tijeras: ").lower()

    if optionUser in ["piedra", "papel", "tijeras"]:
        # Ejecutar el juego con la opción del usuario
        game(optionUser)
        repeat= input("Quieres volver a jugar? (y/n): ")
        if(repeat == "n"):
            count = False
    else:
        print("Por favor, elige una opción válida: piedra, papel o tijeras.")
        repeat= input("Quieres volver a jugar? (y/n): ")
        if(repeat == "n"):
           count = False
