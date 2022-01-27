from operator import index

def generateGrid(keyWord):
    framework = []

    for i in range(len(keyWord)):
        framework.append(keyWord[i])
    
    for i in range(ord('A'), ord('Z') + 1):
        if keyWord.find(chr(i)) != -1 or chr(i) == 'J':
            continue

        framework.append(chr(i))

    return framework

framework = generateGrid('TUES')

def encrypt(secretInfo):
    secretInfo = secretInfo.upper()
    secretInfo = secretInfo.replace(' ', '')
    secretInfo = secretInfo.replace('J', 'I')

    if len(secretInfo) % 2 != 0:
        secretInfo += 'X'

    parted = []
    shred = ''

    for i in range(len(secretInfo)):
        shred += secretInfo[i]

        if i % 2 != 0 or i == len(secretInfo) - 1:
            parted.append(shred)
            shred = ''

    for i in range(len(parted)):
        if parted[i][0] == parted[i][1]:
            parted[i] = parted[i][:-1]
            parted[i] += 'X'
        

    shred = ''
    crypt = []

    for i in parted:
        i1 = 0
        i2 = 0

        for j in range(len(framework)):
            if i[0] == framework[j]:
                i1 = j

            if i[1] == framework[j]:
                i2 = j

        if i1 < i2:
            if i1 - i2 < 5:
                if i1 % 5 != 4:
                    i1 += 1
                else:
                    i1 -= 4
                i2 += 1

            elif i1 % 5 > i2 % 5:
                rowVariance = 0

                while i2 - 5 > i1:
                    i2 -= 5
                    rowVariance += 1

                i1 += rowVariance * 5

            elif i1 % 5 < i2 % 5:
                rowVariance = 0

                while i1 + 5 < i2:
                    i1 += 5
                    rowVariance += 1

                i2 -= rowVariance * 5

            elif i1 % 5 == i2 % 5:
                if i2 + 5 > len(framework) - 1:
                    i2 -= 20
                else:
                    i2 += 5
                
                i1 += 5
            
        else:
            if i2 - i1 < 5:
                if i2 % 5 != 4:
                    i2 += 1
                else:
                    i2 -= 4
                i1 += 1

            elif i2 % 5 > i1 % 5:
                rowVariance = 0

                while i1 - 5 > i2:
                    i1 -= 5
                    rowVariance += 1

                i2 += rowVariance * 5

            elif i2 % 5 < i1 % 5:
                rowVariance = 0

                while i2 + 5 < i1:
                    i2 += 5
                    rowVariance += 1

                i1 -= rowVariance * 5

            elif i2 % 5 == i1 % 5:
                if i1 + 5 > len(framework) - 1:
                    i1 -= 20
                else:
                    i1 += 5
                
                i2 += 5

        shred += framework[i1]
        shred += framework[i2]

        crypt.append(shred)
        shred = ''

    scryptMessage = ''

    return (scryptMessage.join(crypt))

print(encrypt('Hello world!'))

