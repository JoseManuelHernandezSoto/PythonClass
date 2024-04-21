###
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés porcentual anual 
# y el número de años. Muestre el capital obtenido de la inversión cada año que dura la inversión.
#
# Ejemplo
#
# Entrada:
# ¿Cantidad a invertir?: 1000
# ¿Interés porcentual anual?: 10
# ¿Años?: 5
#
# Salida:
# Capital tras 1 año: 1100.0
# Capital tras 2 años: 1210.0
# Capital tras 3 años: 1331.0
# Capital tras 4 años: 1464.1
# Capital tras 5 años: 1610.51
###
money = float(input('Cantidad de dinero a invertir?: '))
interest = int(input('Intereses porcentual anual?'))
years = int(input('Cantidad de años?: '))

for year in range(1, years + 1):
    money += money * (interest / 100)
    print('Capital tras el año {}: {}'.format(year, money))