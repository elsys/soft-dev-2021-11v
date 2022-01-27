
from os import read


key_word = "TUES"
alphabet = list("ABCDEFGHIKLMNOPQRSTUVWXYZ")
i = 0


i = 0
ready_letters = ""
ready_letters = ready_letters + key_word

while i < 25 :
    if alphabet[i] not in key_word:
        ready_letters = ready_letters + alphabet[i]
    print(ready_letters[i], end = "")
    if (i + 1) % 5 == 0 :
        print("")
    i += 1

message = list("SNACKS")
splitted_message = list("")
lenght = len(message)

j = 0
while j < len(message) - 1:
    if(message[j] == " "):
        lenght -= 1
        j += 1

    if(message[j] == message[j + 1]):
        splitted_message += message[j] + "X"
        j += 1

    if(message[j + 1] != " "):
        splitted_message += message[j] + message[j + 1]
    else:
        splitted_message += message[j] + message[j + 2]
        lenght -= 1
        j += 1
    j += 2


if(lenght % 2 != 0):
    if(len(message) == j):
        splitted_message +=  "X"
    else:
        splitted_message += message[-1] + "X"
    
crypted = list("")
index = 2
while index < lenght + 2:
    x1 = x2 = 0
    y1 = y2 = 0
    i = index - 2
    while i < index:
        for j in range(25):
            if(ready_letters[j] == splitted_message[i] and i % 2 == 0):
                x1 = j % 5
                y1 = j // 5
            elif(ready_letters[j] == splitted_message[i] and i % 2 == 1):
                x2 = j % 5
                y2 = j // 5
        i += 1

    if(y1 == y2):
        crypted += ready_letters[y1 * 5 + x1 + 1] + ready_letters[y2 * 5 + x2 + 1]
    elif(x1 == x2):
        crypted += ready_letters[(y1 + 1) * 5 + x1] + ready_letters[(y2 + 1) * 5 + x2]
    elif(x1 != x2 and y1 != y2):
        crypted += ready_letters[y1 * 5 + x2] + ready_letters[y2 * 5 + x1]
    index += 2
    
print(crypted)

