def CreateMatrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    arrangement_of_letters = list(key)

    for j in range(len(key)):
        if arrangement_of_letters[j] == "J":
            arrangement_of_letters[j] = "I"

    for letter in alphabet:
        if letter not in arrangement_of_letters:
            arrangement_of_letters.append(letter)

    matrix = [[0 for i in range (5)] for j in range(5)] 

    index = 0
    for row in range(5):
        for col in range(5):
            matrix[row][col] = arrangement_of_letters[index]
            index += 1
    
    return matrix

def ConvertToDiagraphs(text):
    for index in range(len(text)+1):
        if index < len(text)-1:
            if text[index] == text[index + 1]:
                text = text[:index+1]+'X'+text[index+1:]

    if len(text)%2 != 0:
        text = text[:]+'X'

    return text

def FindIndex (letter, text):
    indexOfChar = []

    if letter == "J":
        letter = "I"

    for i,j in enumerate(text):   # ['T', 'U', 'E', 'S', 'A'],
        for k,l in enumerate(j):  # [(0,'T'),(1,'U'),(2,'E'),(3,'S'),(4,'A')]
            if letter == l:
                indexOfChar.append(i)
                indexOfChar.append(k) 
                return indexOfChar


def encryption (matrix, text):
    cipherText = []

    letter = 0
    while letter < len(text):
        character1 = FindIndex(text[letter], matrix)
        character2 = FindIndex(text[letter+1], matrix)

        # same column 
        if character1[1] == character2[1]:
            i1 = (character1[0] + 1) % 5  #to make value bound under 0 to 4 we will do %5
            j1 = character1[1]

            i2 = (character2[0] + 1) % 5
            j2 = character2[1]
            
            cipherText.append(matrix[i1][j1])
            cipherText.append(matrix[i2][j2])
            cipherText.append(" ")

        # same row
        elif character1[0]==character2[0]:
            i1= character1[0]
            j1= (character1[1] + 1) % 5


            i2 = character2[0]
            j2 = (character2[1] + 1) % 5
            cipherText.append(matrix[i1][j1])
            cipherText.append(matrix[i2][j2])
            cipherText.append(" ")

        # rectangle
        else:
            i1 = character1[0]
            j1 = character1[1]

            i2 = character2[0]
            j2 = character2[1]

            cipherText.append(matrix[i1][j2])
            cipherText.append(matrix[i2][j1])
            cipherText.append(" ")

        letter += 2  

    return " ".join(cipherText)


def main():
    key ="TUES"
    text = input("Text: ").replace(" ","").upper()

    matrix = CreateMatrix(key)
    converted_text = ConvertToDiagraphs(text)
    cipherText = encryption(matrix, converted_text)
    print(cipherText)

if __name__ == "__main__":
    main()
