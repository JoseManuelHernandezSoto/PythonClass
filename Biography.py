count=True
while count== True:
    name = input("Ingresa tu nombre:  ")
    option = input("Tu nombre es correcto?(y/n):  ")
    if(option=="y"):
        count = False

count=True
while count== True:
    birthDate = input("Ingresa tu fecha de nacimiento:  ")
    option = input("Tu fecha de nacimiento es correcta?(y/n):  ")
    if(option=="y"):
        count = False

count=True
while count== True:
    address = input("Ingresa tu direccion:  ")
    option = input("Tu direccion es correcta?(y/n):  ")
    if(option=="y"):
        count = False

count=True
while count== True:
    goal = input("Ingresa una meta personas:  ")
    option = input("Tu meta es correcta?(y/n):  ")
    if(option=="y"):
        count = False

print("- Name: ",name)
print("- Date of birth: ",birthDate)
print("- Address: ",address)
print("- Personal Goals: ",goal)