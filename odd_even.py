# Se crea un ciclo
count = True
while count== True:
    # Se ingresa un numero
    number = int(input("Ingresa un numero entre 1 - 1000:"))

    ###
    ### Si el numero ingresaso cumple los parametros
    ###
    if(number >= 1 and number <=1000):
        # Obtener el modulo del numero
        oddEven = number % 2
        # comparamos el modulo 
        ##
        ## El numero es par
        ##
        if(oddEven==0):
            print("El numero ",number," es par")
            # Se pregunta si quiere repetir el proceso
            repeat= input("Quieres ingresar otro numero? (y/n): ")
            if(repeat == "n"):
                count = False
        ##
        ## Si no es par es impar
        ##
        else:
            print("El numero ",number," es inpar")
            # Se pregunta si quiere repetir el proceso
            repeat= input("Quieres ingresar otro numero? (y/n): ")
            if(repeat == "n"):
                count = False
    # Si el numero no cumple los parametros 
    else:
        print("Numero fuera del rango favor de ingresar otro")


