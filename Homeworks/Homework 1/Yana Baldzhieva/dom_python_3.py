def encrypt(matrix, message):
    for i in matrix:
        if message[0] in i:
            row1 = matrix.index(i)
            col1 = i.index(message[0])
        if message[1] in i:
            row2 = matrix.index(i)
            col2 = i.index(message[1])
    
    if row1 == row2:
        if col1 == 4 and col2 != 4:
            ct = matrix[row1][0] + matrix[row1][col2 + 1]
        elif col1 != 4 and col2 == 4:
            ct = matrix[row1][col1 + 1]+matrix[row1][0]
        elif col1 == 4 and col2 == 4:
            ct = matrix[row1][0] + matrix[row1][0]
        else:
            ct = matrix[row1][col1 + 1] + matrix[row1][col2 + 1]
    
    elif col1 == col2:
        if row1 == 4 and row2 != 4:
            ct = matrix[0][col1] + matrix[row2 + 1][col1]
        elif row1 != 4 and row2 == 4:
            ct = matrix[row1 + 1][col1] + matrix[0][col1]
        elif row1 == 4 and row2 == 4:
            ct = matrix[0][col1] + matrix[0][col1]
        else:
            ct = matrix[row1 + 1][col1] + matrix[row1 + 1][col2]

    else:
        ct = matrix[row1][col2] + matrix[row2][col1] 
    return ct



def decrypt(matrix, ct):
    for i in matrix:
        if ct[0] in i:
            row1 = matrix.index(i)
            col1 = i.index(ct[0])
        if ct[1] in i:
            row2 = matrix.index(i)
            col2 = i.index(ct[1])
    
    if row1 == row2:
        if col1 == 0 and col2 != 0:
            ct = matrix[row1][4] + matrix[row1][col2 - 1]
        elif col1 != 0 and col2 == 0:
            ct = matrix[row1][col1 - 1] + matrix[row1][4]
        elif col1 == 0 and col2 == 0:
            ct = matrix[row1][4] + matrix[row1][4]
        else:
            ct = matrix[row1][col1 - 1] + matrix[row1][col2 - 1]
    
    elif col1 == col2:
        if row1 == 0 and row2 != 0:
            ct = matrix[4][col1] + matrix[row2 - 1][col1]
        elif row1 != 0 and row2 == 0:
            ct = matrix[row1 - 1][col1] + matrix[4][col1]
        elif row1 == 0 and row2 == 0:
            ct = matrix[4][col1] + matrix[4][col1]
        else:
            ct = matrix[row1 - 1][col1] + matrix[row1 - 1][col2]
            
    else:
        ct = matrix[row1][col2] + matrix[row2][col1] 
    return ct





matrix = [['T', 'U', 'E', 'S', 'A'], 
            ['B', 'C', 'D', 'F', 'G'], 
            ['H', 'I', 'K', 'L', 'M'], 
            ['N', 'O', 'P', 'Q', 'R'],
            ['V', 'W', 'X', 'Y', 'Z']]
test_message = "Hello"
test_message = test_message.replace("J", "I")
test_message = test_message.upper()
for i in range(len(test_message) - 1):
    if test_message[i] == test_message[i+1]:
        test_message = test_message[:i + 1] + "X" + test_message[i + 1:]



test_message = list(test_message.replace(" ",""))
if len(test_message) % 2 != 0:
    test_message.append('X')

print(test_message)
init_blocks = list()
index = 0

for i in list(range(int(len(test_message)/2))):
    block = test_message[index:index+2]
    index = index + 2
    init_blocks.append(block)

index = 0
blocks = []
for i in list(range(int(len(init_blocks)/10) + 1)):
    block = init_blocks[index:index + 10]
    index = index + 10
    blocks.append(block)
final_ct = []
for main_block in blocks:
    ct = []
    for blocks in main_block:
        ct.append(encrypt(matrix, blocks))
    final_ct.append(ct)
    

print("Encrypted text ", final_ct)


decrypted_pt = []
for main_block in final_ct:
    temp_pt = []
    for block in main_block:
        temp_pt.append(decrypt(matrix,block))
    decrypted_pt.append(temp_pt)
    

print("Decrypted text ",decrypted_pt)