#Creamos un contador para que entre al ciclo y pueda salir tambien
count=True
while count== True:
    #Solicitamos el nombre del usuario
    name = input("Ingresa tu nombre:  ")
    #Preguntamos si el dato es correcto en caso afirmativo sale del clico
    #si la respuesta es negativa se repite el ciclo y se volvera a pedir el nombre
    option = input("Tu nombre es correcto?(y/n):  ")
    if(option=="y"):
        #Se el valor para poder salir del ciclo
        count = False

#Se repiten los mismos pasos que con el nombre 
count=True
while count== True:
    birthDate = input("Ingresa tu fecha de nacimiento:  ")
    option = input("Tu fecha de nacimiento es correcta?(y/n):  ")
    if(option=="y"):
        count = False


#Se repiten los mismos pasos que con el nombre 
count=True
while count== True:
    address = input("Ingresa tu direccion:  ")
    option = input("Tu direccion es correcta?(y/n):  ")
    if(option=="y"):
        count = False


#Se repiten los mismos pasos que con el nombre 
count=True
while count== True:
    goal = input("Ingresa una meta personas:  ")
    option = input("Tu meta es correcta?(y/n):  ")
    if(option=="y"):
        count = False

#Cuando es usuario confirma todos los datos se imprime el siguiente formato
#con los datos del usuario 
print("- Name: ",name)
print("- Date of birth: ",birthDate)
print("- Address: ",address)
print("- Personal Goals: ",goal)