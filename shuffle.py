import random
# Declaramos el arreglo de numbers
numbers=[]
iteration=[]
shuffle=[]
# Recibimos la cantidad de numeros que va a tener nuestro arreglo
cant= int(input('Ingresa la cantidad de numeros de la lista: '))

for i in range(cant):
    # agregarmos numeros aleatorios a 'numbers'
    numbers.append(random.randrange(1,100))
    # agregamos numeros unicos dentro del rango de 'cant'
    iteration = random.sample(range(cant), cant)

    shuffle.append(0)

# Imprimimos el arreglo
print(numbers)
#print(iteration)

for i in range(cant):
    local2= iteration[i-1]
    local = numbers[i-1]
    shuffle[local2] = local

numbers = shuffle
print(numbers)