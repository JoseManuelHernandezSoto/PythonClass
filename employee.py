###
# En una determinada empresa, sus empleados son evaluados cada seis meses. 
# Los puntos que pueden obtener en la evaluación comienzan en 0 y pueden ir aumentando hasta llegar a 10, 
# traduciéndose en mejores beneficios (al final del problema se muestra una tabla con los niveles 
# correspondientes a cada puntuación). La cantidad de dinero conseguida en cada nivel se calcula 
# multiplicando el "salario mensual" por la división de la "puntuación del nivel" dividida entre "10". 
#
# Escribir un programa que lea la puntuación del usuario y su salario mensual e imprima su nivel de 
# rendimiento, así como la cantidad de dinero que recibirá el usuario. 
#
# Ejemplo: 
#
# Salario =  10,000
# Puntuación = 8
# Dinero = 10,000 * (8/10) = 8000. 
# Resultado =  Nivel de Rendimiento "Meritorio", Cantidad de Dinero Recibido $8000
#
# NIVEL --------------------------------- PUNTUACIÓN
# Inaceptable ------------------------   0 a 3
# Aceptable ---------------------------  4 a 6
# Meritorio -----------------------------  7 a 10
###
wage = float(input('Ingresa la paga del empleado: '))
points = int(input('Ingresa la cantidad de puntos del empleado: '))
pay = float(wage * (points/10))

if points in range(0,3):
    level = 'Inaceptable'
elif points in range(4,6):
    level = 'Aceptaeble'
elif points in range(7,10):
    level = 'Meritorio'

print('Nivel de rendimiento "{}" , Cantidad de dinero recibido ${}'.format(level,pay))