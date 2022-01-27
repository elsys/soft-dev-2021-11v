# Yordan Markov N15 11v
# Playfair

# GLOBAL
matrix = [['T', 'U', 'E', 'S', 'A'], 
          ['B', 'C', 'D', 'F', 'G'], 
          ['H', 'I', 'K', 'L', 'M'], # Only I (J is I)
          ['N', 'O', 'P', 'Q', 'R'],
          ['V', 'W', 'X', 'Y', 'Z']]

def get_index(letter):
    for m in range(5):  
        for n in range(5):
            if letter == matrix[m][n]:
                return (m, n)

def encrypt(message):
    message = message.upper()
    message = message.replace('J', 'I')
    message = message.replace(' ', '')
    for i in range(len(message) - 1):
        if message[i] == message[i + 1]:
            message = message[:i + 1] + "X" + message[i + 1:]
    if len(message) % 2 != 0:
        message += "X"
    message = list(message)
    coords = []
    for i in range(0, len(message) - 1, 2):
        coords = [get_index(message[i]), get_index(message[i + 1])] # coords[0][0] = 1 element x...
        if coords[0][0] == coords[1][0]: # They are on the same row
            changable = coords[0][1] + 1
            if changable > 4:
                changable = 0
            message[i + 1] = matrix[coords[0][0]][changable]
            changable = coords[1][1] + 1
            if changable > 4:
                changable = 0
            message[i] = matrix[coords[1][0]][changable]
        elif coords[0][1] == coords[1][1]: # They are on the same column
            changable = coords[0][0] + 1
            if changable > 4:
                changable = 0
            message[i] = matrix[changable][coords[0][1]]
            changable = coords[1][0] + 1
            if changable > 4:
                changable = 0
            message[i + 1] = matrix[changable][coords[1][1]]
        else:
            message[i + 1] = matrix[coords[1][0]][coords[0][1]]
            message[i] = matrix[coords[0][0]][coords[1][1]]
    print(''.join(message))

def decrypt(message):
    message = message.upper()
    message = message.replace('J', 'I')
    message = message.replace(' ', '')
    for i in range(len(message) - 1):
        if message[i] == message[i + 1]:
            message = message[:i + 1] + "X" + message[i + 1:]
    if len(message) % 2 != 0:
        message += "X"
    message = list(message)
    coords = []
    for i in range(0, len(message) - 1, 2):
        coords = [get_index(message[i]), get_index(message[i + 1])] # coords[0][0] = 1 element x...
        if coords[0][0] == coords[1][0]: # They are on the same row
            changable = coords[0][1] - 1
            if changable < 0:
                changable = 4
            message[i + 1] = matrix[coords[0][0]][changable]
            changable = coords[1][1] - 1
            if changable < 0:
                changable = 4
            message[i] = matrix[coords[1][0]][changable]
        elif coords[0][1] == coords[1][1]: # They are on the same column
            changable = coords[0][0] - 1
            if changable < 0:
                changable = 4
            message[i] = matrix[changable][coords[0][1]]
            changable = coords[1][0] - 1
            if changable < 0:
                changable = 4
            message[i + 1] = matrix[changable][coords[1][1]]
        else:
            message[i + 1] = matrix[coords[1][0]][coords[0][1]]
            message[i] = matrix[coords[0][0]][coords[1][1]]
    print(''.join(message))

def main():
    # Let's encrypt a sentence!
    encrypt("Hello World")
    # Let's decrypt a sentence!
    decrypt("KTKYIQUWQMKE")

# Runs our main function
if __name__ == "__main__":
    main()