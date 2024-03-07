#Se pide al usuario que ingrese la cuenta
check = float(input("¿Cuánto es la cuenta? "))
#Preguntamos cuanto es lo que va a dejar de propina si el 18%, 20% o 25%
tip = input("¿Cuánto vamos a dejar de propina?\n 1) 18%\n 2) 20%\n 3) 25%\n")
#Preguntamos cuantas personas hay en la mesa para poder dividir la cuenta de manera igual
persons = int(input("¿Cuantas personas hay en la mesa?"))
###
### Dependiendo de la eleccion del usuario al momento de dejar 
### propina se crea la variable 'percentage' y se le asigna un valor 
###
if tip == '1':
    percentage = 0.18
elif tip == '2':
    percentage = 0.20
elif tip == '3':
    percentage = 0.25
else:
    #   Si no ingresa un numero del 1 al 3 aparece lo siguiente
    print("Opción inválida")
    exit()  # Salir del programa si la opción de propina es inválida

##
## Creamos la variable total y realizamos las operacion para calcular cuanto se tiene que pagar  
##
total = (check * (1 + percentage)) / persons

## Mostramos al usuario el resultado
print("El total a pagar entre ",persons," con una propina del", percentage * 100, "% es  de:", total)
