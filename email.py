# Pedimos un correo al usuario
email = input("ingresa tu correo elecatronico:  ").strip()
# Creamos la variable 'username' y se almacena todo lo que esta antes del @ del correo
username= email[:email.index('@')]
# Creamos la variable 'domain' y se almacena todo lo que esta despues del @ del correo
domain = email[email.index('@')+1:]
###
### un IF en el que dependiendo del domino del usuario le asegnamos un valor a 
### la variable 'annex' 
###
if domain == "gmail.com":
    annex = "tu dominio es de google genial!!!"
elif domain == "outlook.com":
    annex = "tu dominio es de microsoft genial!!!"
elif domain == "hotmail.com":
    annex = "tu dominio es de microsoft genial!!!"
else:
    annex = "tu dominio es genial!!!"
###
### Creamos una cadena de texto para crear un mensaje que mostraremos al usuario con los datos del correo
###
result = "Tu nombre de ususario es: "+username+"\nTu dominio es: "+domain+" "+annex
print(result)