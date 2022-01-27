def addBogusLetters(text):
    for s in range(0, len(text), 2):
        if s < (len(text) - 1):
            if text[s] == text[s + 1]:
                text = text[:s + 1] + 'x' + text[s + 1:]
    if len(text) % 2 != 0:
        text = text[:] + 'x'
    return text
def locateIndex(char, matrix):
    
    if char == "J" or char == "I":
        char = "IJ"
    indexOfChar = []
    for i,j in enumerate(matrix):
        for k,l in enumerate(j):
            if char == l:
                indexOfChar.append(i)
                indexOfChar.append(k)
                return indexOfChar

def encryptCipher(text):
    text = text.upper()
    matrix = ['T', 'U', 'E', 'S', 'A'], ['B', 'C', 'D', 'F', 'G'], ['H', 'IJ', 'K', 'L', 'M'], ['N', 'O', 'P', 'Q', 'R'], ['V', 'W', 'X', 'Y', 'Z']
    cipherText = []
    i = 0
    
    while i < len(text):
        letter1 = locateIndex(text[i], matrix)

        letter2 = locateIndex(text[i + 1], matrix)
        
        if letter1[1] == letter2[1]:
            newLetterX1 = (letter1[0] + 1) % 5
            newLetterY1 = letter1[1]

            newLetterX2 = (letter2[0] + 1) % 5
            newLetterY2 = letter2[1]

            cipherText.append(matrix[newLetterX1][newLetterY1])
            cipherText.append(matrix[newLetterX2][newLetterY2])

        elif letter1[0] == letter2[0]:
            newLetterX1 = letter1[0]
            newLetterY1 = (letter1[1] + 1) % 5

            newLetterX2 = letter2[0]
            newLetterY2 = (letter2[1] + 1) % 5

            cipherText.append(matrix[newLetterX1][newLetterY1])
            cipherText.append(matrix[newLetterX2][newLetterY2])

        else:
            newLetterX1 = letter1[0]
            newLetterY1 = letter1[1]
            newLetterX2 = letter2[0]
            newLetterY2 = letter2[1]
            cipherText.append(matrix[newLetterX1][newLetterY2])
            cipherText.append(matrix[newLetterX2][newLetterY1])
        
        i += 2
    return cipherText

text = "jorom"

text = addBogusLetters(text)

print(encryptCipher(text))
