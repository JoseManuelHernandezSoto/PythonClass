# Importamos el modulo 'lyrics' donde estan las letras de las canciones
import lyrics

# Diccionario con el título de las canciones como clave y la letra como valor
songs = {
    "Green Day - Holiday": lyrics.Holiday,
    "The Killers - Mr. Brightside": lyrics.mrBrightside,
    "Green Day - Boulevard Of Broken Dreams": lyrics.boulevardOfBrokenDreams,
    "Green Day - American Idiot": lyrics.americanIdiot,
    "Bon Jovi - Livin' On A Prayer": lyrics.livingOnAPlayer,
    "Foo Fighters - The Pretender": lyrics.pretender,
    "Papa Roach - Last Resort": lyrics.lastResort,
    "System Of A Down - Aerials": lyrics.Aerials,
    "System Of A Down - Question!": lyrics.question,
    "System Of A Down - Hypnotize": lyrics.hypnotize,
    "System Of A Down - Lonely Day": lyrics.lonelyDay,   
}

# Imprime la lista de canciones
print("Lista de canciones:")
for i, song in enumerate(songs, 1):
    print(f"{i}. {song}")

# Pedir al usuario que elija una canción
option = int(input("Elige una canción (1-11): "))

# Verificar si la opción del usuario es válida
if option < 1 or option > 11:
    print("Opción inválida")
else:
    # Obtener el título de la canción seleccionada
    songTitle = list(songs.keys())[option - 1]
    
    # Obtener la letra de la canción seleccionada
    songLyrics = songs[songTitle]
    
    # Imprimir la letra de la canción seleccionada
    print(f"\nElejiste: '{songTitle}' Aqui tienes. \n --------------- {songTitle}--------------- \n{songLyrics}")
