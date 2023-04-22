import sys

def log(*x):
    print(" == ", x, file=sys.stderr, flush=True)

n = int(input())
table = {}
for i in range(n):
    inputs = input().split()
    b = inputs[0]
    c = int(inputs[1])
    table[b] = c
word = input()

def decode_word(table, word):
    """
    Fonction généré par ChatGPT

    [FR]
    La fonction decode_word prend en entrée le dictionnaire table et la chaîne word.
    La variable decoded_word est initialisée à une chaîne vide qui sera remplie au fur et à mesure que chaque partie de word sera décodée.
    La variable i est initialisée à zéro pour garder une trace de l'index actuel de word.
    La boucle externe parcourt chaque caractère de word un par un.
    La boucle interne vérifie chaque sous-chaîne de word à partir de l'index i jusqu'à la fin de la chaîne pour voir si elle est dans le dictionnaire table.
    Si une sous-chaîne correspondante est trouvée, on ajoute le caractère ASCII correspondant à decoded_word et on met à jour i pour continuer à parcourir word à partir de l'index suivant.
    Si aucune sous-chaîne correspondante n'est trouvée, on imprime un message d'erreur et on arrête le décodage.
    À la fin de chaque boucle externe, on incrémente i pour passer au caractère suivant.
    Si la boucle externe se termine avec succès, cela signifie que word a été entièrement décodé et on imprime la chaîne décodée.

    [Eng]
    The decode_word function takes the table dictionary and the word string as input.
    The decoded_word variable is initialized to an empty string that will be filled as each part of word is decoded.
    The i variable is initialized to zero to keep track of the current index of word.
    The outer loop iterates through each character of word one by one.
    The inner loop checks each substring of word from index i to the end of the string to see if it is in the table dictionary.
    If a matching substring is found, the corresponding ASCII character is added to decoded_word and i is updated to continue iterating through word from the next index.
    If no matching substring is found, an error message is printed and the decoding is stopped.
    At the end of each outer loop, i is incremented to move to the next character.
    If the outer loop finishes successfully, this means that word has been fully decoded and the decoded string is printed.

    """
    decoded_word = ""
    i = 0
    while i < len(word):
        for j in range(i, len(word)):
            if word[i:j+1] in table:
                decoded_word += chr(table[word[i:j+1]])
                i = j+1
                break
        else:
            print(f"DECODE FAIL AT INDEX {i}")
            return
    print(decoded_word)

decode_word(table, word)
