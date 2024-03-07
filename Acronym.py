def generar_acronimo(sentence):
    words = sentence.split()
    acronym = ""
    for word in words:
        acronym += word[0].upper()
    return acronym

sentence = input("Ingresa una frase para generar un acrónimo: ")
acr = generar_acronimo(sentence)
print("El acrónimo de la frase es:", acr)