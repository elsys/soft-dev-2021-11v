# T U E S A
# B C D F G
# H I K L M
# N O P Q R
# V W X Y Z

#pravim si matricata
table = []
alphabet = "TUESABCDFGHIKLMNOPQRVWXYZ"
for i in range(5):
    row = []
    for j in range(i*5, i*5 + 5):
        row.append(alphabet[j])
    table.append(row)

#formatirane na izrechenieto za kodirane
sentence = "cq uy cf bn pr qy qr" #str(input())
# [F,O] [S,W] [D,G] [H,V] [Q,N] [Y,S] [R,N]
sentence = ''.join(sentence.split())
sentence = sentence.upper()

#proverki za ednakvi bukvi i J
for i in range(len(sentence)-1):
    if(sentence[i] == sentence[i+1]):
        sentence = sentence[:i+1] + "X" + sentence[i+1:]
    if(sentence[i] == 'J'):
        sentence = sentence.replace("J", "I")

#broi na dvoikite na koito se razdelq
if (int((len(sentence)))%2) == 1:
    sentence += "X"
couples = len(sentence)/2

#razdelqne na samoto izrechenie
splitSentence = []
for i in range(int(couples)):
    couple = []
    for j in range (i*2, i*2 + 2):
        couple.append(sentence[j])
    splitSentence.append(couple)

for i in range(len(splitSentence)):
    current = list()
    current = splitSentence[i]
    for k in range(5):
        for l in range(5):
            #vzimame indeksite na bukvite
            if(current[0] == table[k][l]):
                firstIndexes = [k,l]
            if(current[1] == table[k][l]):
                secondIndexes = [k,l]
    #ako sa na edin red 
    if(firstIndexes[0] == secondIndexes[0]):
        if(firstIndexes[1] == 4):
            current[0] = table[firstIndexes[0]][0]
        else:
            current[0] = table[firstIndexes[0]][firstIndexes[1]+1]
        if(secondIndexes[1] == 4):
            current[1] = table[secondIndexes[0]][0]
        else:
            current[1] = table[secondIndexes[0]][secondIndexes[1]+1]
        splitSentence[i] = current
    #ako sa na edna kolona i edno do drugo
    elif(firstIndexes[1] == secondIndexes[1]):
        if(firstIndexes[0] == 4):
            current[0] = table[0][firstIndexes[1]]
        else:
            current[0] = table[firstIndexes[0]+1][firstIndexes[1]]
        if(secondIndexes[0] == 4):
            current[1] = table[0][secondIndexes[1]]
        else:
            current[1] = table[secondIndexes[0]+1][secondIndexes[1]]
        splitSentence[i] = current
    #ako e za kvadrat
    else:
        current[0] = table[firstIndexes[0]][secondIndexes[1]]
        current[1] = table[secondIndexes[0]][firstIndexes[1]]
        splitSentence[i] = current

print("Decrypted message ", splitSentence)