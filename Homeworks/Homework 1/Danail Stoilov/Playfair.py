from operator import index


def generateGrid(keyword):
    grid = []
    for i in range(len(keyword)):
        grid.append(keyword[i])
    
    for i in range(ord('A'), ord('Z') + 1):
        if keyword.find(chr(i)) != -1 or chr(i) == 'J':
            continue

        grid.append(chr(i))

    return grid

grid = generateGrid('TUES')

# ['T', 'U', 'E', 'S', 'A']
# ['B', 'C', 'D', 'F', 'G']
# ['H', 'I', 'K', 'L', 'M']
# ['N', 'O', 'P', 'Q', 'R']
# ['V', 'W', 'X', 'Y', 'Z']

def encrypt(message):
    message = message.upper()
    message = message.replace(' ', '')
    message = message.replace('J', 'I')

    if len(message) % 2 != 0:
        message += 'X'

    separate = []
    piece = ''
    for i in range(len(message)):
        piece += message[i]

        if i % 2 != 0 or i == len(message) - 1:
            separate.append(piece)
            piece = ''

    for i in range(len(separate)):
        if separate[i][0] == separate[i][1]:
            separate[i] = separate[i][:-1]
            separate[i] += 'X'
        

    piece = ''
    encryption = []
    for i in separate:
        index1 = 0
        index2 = 0

        for j in range(len(grid)):
            if i[0] == grid[j]:
                index1 = j

            if i[1] == grid[j]:
                index2 = j

        if index1 < index2:
            if index1 - index2 < 5:
                if index1 % 5 != 4:
                    index1 += 1
                else:
                    index1 -= 4
                index2 += 1

            elif index1 % 5 > index2 % 5:
                rowDifference = 0

                while index2 - 5 > index1:
                    index2 -= 5
                    rowDifference += 1

                index1 += rowDifference * 5

            elif index1 % 5 < index2 % 5:
                rowDifference = 0

                while index1 + 5 < index2:
                    index1 += 5
                    rowDifference += 1

                index2 -= rowDifference * 5

            elif index1 % 5 == index2 % 5:
                if index2 + 5 > len(grid) - 1:
                    index2 -= 20
                else:
                    index2 += 5
                
                index1 += 5
            
        else:
            if index2 - index1 < 5:
                if index2 % 5 != 4:
                    index2 += 1
                else:
                    index2 -= 4
                index1 += 1

            elif index2 % 5 > index1 % 5:
                rowDifference = 0

                while index1 - 5 > index2:
                    index1 -= 5
                    rowDifference += 1

                index2 += rowDifference * 5

            elif index2 % 5 < index1 % 5:
                rowDifference = 0

                while index2 + 5 < index1:
                    index2 += 5
                    rowDifference += 1

                index1 -= rowDifference * 5

            elif index2 % 5 == index1 % 5:
                if index1 + 5 > len(grid) - 1:
                    index1 -= 20
                else:
                    index1 += 5
                
                index2 += 5

        piece += grid[index1]
        piece += grid[index2]
        encryption.append(piece)
        piece = ''

    encryptedMessage = ''
    return (encryptedMessage.join(encryption))

print(encrypt('hide the gold in the tree stump'))