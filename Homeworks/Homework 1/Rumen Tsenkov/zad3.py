from operator import index


def Grid(key):
    grid = []
    for n in range(len(key)):
        grid.append(key[n])
    
    for i in range(ord('A'), ord('Z') + 1):
        if key.find(chr(i)) != -1 or chr(i) == 'J':
            continue

        grid.append(chr(i))

    return grid

grid = Grid('TUES')


def encrypt_message(message):
    message = message.upper()
    message = message.replace(' ', '')
    message = message.replace('J', 'I')

    if len(message) % 2 != 0:
        message += 'X'

    separation = []
    bit = ''
    for i in range(len(message)):
        bit += message[i]

        if i % 2 != 0 or i == len(message) - 1:
            separation.append(bit)
            bit = ''

    for i in range(len(separation)):
        if separation[i][0] == separation[i][1]:
            separation[i] = separation[i][:-1]
            separation[i] += 'X'
        

    bit = ''
    encryption = []
    for i in separation:
        ind1 = 0
        ind2 = 0

        for j in range(len(grid)):
            if i[0] == grid[j]:
                ind1 = j

            if i[1] == grid[j]:
                ind2 = j

        if ind1 < ind2:
            if ind1 - ind2 < 5:
                if ind1 % 5 != 4:
                    ind1 += 1
                else:
                    ind1 -= 4
                ind2 += 1

            elif ind1 % 5 > ind2 % 5:
                rowDifference = 0

                while ind2 - 5 > ind1:
                    ind2 -= 5
                    rowDifference += 1

                ind1 += rowDifference * 5

            elif ind1 % 5 < ind2 % 5:
                rowDifference = 0

                while ind1 + 5 < ind2:
                    ind1 += 5
                    rowDifference += 1

                ind2 -= rowDifference * 5

            elif ind1 % 5 == ind2 % 5:
                if ind2 + 5 > len(grid) - 1:
                    ind2 -= 20
                else:
                    ind2 += 5
                
                ind1 += 5
            
        else:
            if ind2 - ind1 < 5:
                if ind2 % 5 != 4:
                    ind2 += 1
                else:
                    ind2 -= 4
                ind1 += 1

            elif ind2 % 5 > ind1 % 5:
                rowDifference = 0

                while ind1 - 5 > ind2:
                    ind1 -= 5
                    rowDifference += 1

                ind2 += rowDifference * 5

            elif ind2 % 5 < ind1 % 5:
                rowDifference = 0

                while ind2 + 5 < ind1:
                    ind2 += 5
                    rowDifference += 1

                ind1 -= rowDifference * 5

            elif ind2 % 5 == ind1 % 5:
                if ind1 + 5 > len(grid) - 1:
                    ind1 -= 20
                else:
                    ind1 += 5
                
                ind2 += 5

        bit += grid[ind1]
        bit += grid[ind2]
        encryption.append(bit)
        bit = ''

    encryptedMessage = ''
    return (encryptedMessage.join(encryption))
print('The enscryped message is:')
print(encrypt_message('fuck the police'))