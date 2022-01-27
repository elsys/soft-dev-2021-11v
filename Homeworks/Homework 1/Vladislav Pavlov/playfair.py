import math

def get_letter_index(cypher, letter):
    for x in range(5):
        for y in range(5):
            if letter == cypher[x][y]:
                return (x, y)

def prepare_for_encryption(word):
    i = 0
    tempword = ""
    while i < len(word):
        tempword += word[i]
        if i != len(word) - 1:
            if word[i] == word[i+1]:
                tempword += 'X'
            else:
                tempword += word[i+1]
                i+=1
        i+=1
    if len(tempword) % 2 != 0:
        tempword += 'X'
    return tempword

def encrypt(word, cypher):
    encrypted = ""
    i = 0
    while i < len(word)-1:
        x1, y1 = get_letter_index(cypher, word[i])
        x2, y2 = get_letter_index(cypher, word[i+1])
        i+=2

        if x1 == x2:
            encrypted+=cypher[x1][ (y1+1) % 5 ]
            encrypted+=cypher[x2][ (y2+1) % 5 ]
        elif y1 == y2:
            encrypted+=cypher[(x1+1) % 5][y1]
            encrypted+=cypher[(x2+1) % 5][y2]
        else:
            encrypted+=cypher[x1][y2]
            encrypted+=cypher[x2][y1]
    return encrypted

def decrypt(word, cypher):
    decrypted = ""
    i = 0
    while i < len(word)-1:
        x1, y1 = get_letter_index(cypher, word[i])
        x2, y2 = get_letter_index(cypher, word[i+1])
        i+=2

        if x1 == x2:
            decrypted+=cypher[x1][y1-1]
            decrypted+=cypher[x2][y2-1]
        elif y1 == y2:
            decrypted+=cypher[x1-1][y1]
            decrypted+=cypher[x2-1][y2]
        else:
            decrypted+=cypher[x1][y2]
            decrypted+=cypher[x2][y1]
    return decrypted

def create_cypher(key):
    alphabet = list("ABCDEFGHIKLMNOPQRSTUVWXYZ");
    cypher = [[], [], [], [], []]
    real_key = []
    for i in key:
        if i not in real_key:
            real_key.append(i)
    for i in real_key:
        for j in alphabet:
            if i == j:
                alphabet.remove(j)


    for letter, i in enumerate(real_key):
        cypher[math.floor(letter/5)].append(i)

    for i in alphabet:
        letter+=1
        cypher[math.floor(letter/5)].append(i)
    
    return cypher

key = list("PLAYFAIREXAMPLE")
word = "hidethegoldinthetreestump"
word = word.upper()
letter = 0;

cypher = create_cypher(key)
encrypted = encrypt(prepare_for_encryption(word),cypher)
print(encrypted)

print(cypher)

decrypted = decrypt(encrypted, cypher)
print(decrypted)

