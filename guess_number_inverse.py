#Importamos la libreria random que sera muy importante
import random
# Creamos la variable 'number' y le asignamos un numero del 1 al 50 al azar
number = random.randrange(1,50)
# Pedimos al usuario ingresar un numero para que adivine la maquina
guess = int(input('Ingresa un numero para que adivine la maquina (debe de ser entre 1 - 50)'))
count = 0
###
### Ciclo de adivinansa
###
while guess != number:
    if guess<1 or guess>50:
        guess = int(input('Ingresa un numero para que adivine la maquina (debe de ser entre 1 - 50)'))
    else:
        count+= 1
        number = random.randrange(1,50)

# Cuando la maquina adivina el numero 
String =  'La maquina tardo {} intentos en adivinar tu numero'.format(count)
print(String)