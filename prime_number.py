def prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def triangle(number):
    if prime(number):
        for i in range(number, 0, -1):
            for j in range(i, number + 1, 2):
                if prime(j):
                    print(j, end=" ")
            print()
    else:
        print("El número ingresado no es primo.")

number = int(input("Ingrese un número entero primo: "))
triangle(number)