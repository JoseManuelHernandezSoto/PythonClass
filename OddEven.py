count = True
while count== True:
    number = int(input("Ingresa un numero entre 1 - 1000:"))

    if(number >= 1 and number <=1000):
        oddEven = number % 2
        if(oddEven==0):
            print("El numero ",number," es par")
            repeat= input("Quieres ingresar otro numero? (y/n): ")
            if(repeat == "n"):
                count = False
        else:
            print("El numero ",number," es inpar")
            repeat= input("Quieres ingresar otro numero? (y/n): ")
            if(repeat == "n"):
                count = False
    else:
        print("Numero fuera del rango favor de ingresar otro")


