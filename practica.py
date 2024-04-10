from colorama import Fore, Style

name = input("Por favor ingresa tu nombre: ")
age = input("Por favor ingresa tu edad: ")
email = input("Por favor ingresa tu dirección de correo: ")

print("Hola, mi nombre es", Fore.YELLOW + name + ",", "mi dirección es", Fore.MAGENTA + email + ",", "y mi edad es", Fore.BLUE + age + ".", Style.RESET_ALL)