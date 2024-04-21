###
# Escribir el código que permita convertir una candad N a monedas. Usar monedas de 
# $20, $10, $5, $1. Importante considerar que la cantidad es un valor entero.
# También se solicita imprimir los mensajes correspondientes. 
# Deberá incluir comentarios en su código para indicar a otros programadores su proceder (sin abusar 🤔).
#
# Ejemplo:
#
# Entrada:
# Cantidad a Convertir : 397
#
# Salida:
# Monedas de $20: 19
# Monedas de $10: 1
# Monedas de $5: 1
# Monedas de $1: 2
###
coin20=0
coin10=0
coin5=0
coin1=0

money = int(input('Ingres la catidad de dinero a convertir: '))

while money > 0:
    if 20 <= money :
        coin20 = money // 20
        money -= coin20 * 20
    elif 10 <= money:
        coin10 = money // 10
        money -= coin10 * 10
    elif 5 <= money:
        coin5 = money // 5
        money -= coin5 * 5
    elif 1 <= money:
        coin1 = money // 1
        money -= coin1 * 1

print('La cantidad de monedas son: \nmonedas de $20: {}\nmonedas de $10: {}\nmonedas de $5 son: {} \nmonedas de $1: {} \nsobra ${}'.format(coin20,coin10,coin5,coin1,money))

    
