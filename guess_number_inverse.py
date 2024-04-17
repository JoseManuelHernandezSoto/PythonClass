#Importamos la libreria random que sera muy importante
import random
# Creamos la variable 'number' y le asignamos un numero del 1 al 50 al azar
min = 1
max = 100
number = random.randrange(min,max)
# Pedimos al usuario ingresar un numero para que adivine la maquina
guess = int(input('Ingresa un numero para que adivine la maquina (debe de ser entre {} - {}): '.format(min,max)))
count = 0
###
### Ciclo de adivinansa
###
while guess != number:
    if guess<min or guess>max:
        guess = int(input('Ingresa un numero para que adivine la maquina (debe de ser entre {} - {})'.format(min,max)))
    else:
        if number < guess:
            min= number
        elif number > guess:
            max = number     

        count+= 1
        print(number)
        number = random.randrange(min,max)

# Cuando la maquina adivina el numero 
String =  'La maquina tardo {} intentos en adivinar tu numero'.format(count)
print(String)