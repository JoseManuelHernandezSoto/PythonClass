# Ingresa una frase
sentence = input("En que estas pensando?:  ")
# Separa la frase en palabras
words = sentence.split()
# Cuentas las palabras 
countWord = len(words)
# Imprime resultado
print("Genial, lo que piensas me lo dices en ",countWord," palabras")