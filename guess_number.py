#Importamos la libreria random que sera muy importante
import random
# Creamos la variable 'number' y le asignamos un numero del 1 al 50 al azar
number = random.randrange(1,50)
# Pedimos al usuario que ingrese un numero para tratar de adivinar el numero que se asigno a 'number'
guess = int(input("Adivinna un numero entre 1 - 50:  "))

###
### Entramos en un ciclo hasta que el usuario encuentre el numero correcto
###
while guess != number:
    # Si el numero que ingreso el usuario es menor que el de 'number' entra aqui 
    if (guess < number):
        print("Elije un numero mas alto. Intentalo otra vez")
        guess = int(input("\nAdivina un numero entre 1 - 50:  "))
    # Si el numero que ingreso el usuario es mayor que el de 'number' entra aqui 
    else:
        print("Elije un numero mas bajo. Intentalo otra vez")
        guess = int(input("\nAdivina un numero entre 1 - 50:  "))
# Cuando el usuario adivina el numero sale del ciclo y lo felicitamos
print("Adivinaste el numero felicidades!!!")