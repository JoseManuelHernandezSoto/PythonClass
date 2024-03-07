def is_palindromo(word):
    # Comparar la palabra con su inversa para determinar si es palíndromo
    return word == word[::-1]

# Pedir al usuario que ingrese 5 palabras
words = []
for i in range(5):
    word = input(f"Ingrese la palabra #{i + 1}: ")
    words.append(word.lower()) 

# Determinar cuáles palabras son palíndromos
palindromes = []
no_palindromes = []
for word in words:
    if is_palindromo(word):
        palindromes.append(word)
    else:
        no_palindromes.append(word)

# Mostrar los resultados
print("\nPalíndromos:")
for palindrome in palindromes:
    print(palindrome)

print("\nNo palíndromos:")
for no_palindrome in no_palindromes:
    print(no_palindrome)
