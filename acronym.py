#Definimos una funcion que genera el acronimo 
def generate_acronym(sentence):
    #Se separa la grase por palabras
    words = sentence.split()
    #Se genera una variable donde vamos a guardar la letras
    acronym = ""
    for word in words:
        #Se almacena la pocision '0' de cada palabra y se transforma en mayuscula
        acronym += word[0].upper()
    #Regresa el resultado
    return acronym
#Se solicita una frace
sentence = input("Ingresa una frase para generar un acrónimo: ")
#Se crea una variable en la se va a almacenar el resultado.
#Se manda a llamar el metodo 'generate_acronym' y se manda como parametro
# la frase que ingreso el usuario
acr = generate_acronym(sentence)
#Se imprime el resultado 
print("El acrónimo de la frase es:", acr)