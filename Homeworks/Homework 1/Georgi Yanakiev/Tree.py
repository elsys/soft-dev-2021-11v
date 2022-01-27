import random

matrix = []

for i in range (100):
    matrix.append([])
    for j in range(i + 1):
        matrix[i].append(random.randint(0, 100))
        print(str(matrix[i][j]) + " ", end = "")
    print("")
    
matrix_rows = len(matrix) - 1


while matrix_rows > 0:
    for j in range(matrix_rows):
        if matrix[matrix_rows][j] > matrix[matrix_rows][j + 1]:
            matrix[matrix_rows - 1][j] += matrix[matrix_rows][j]
        else: 
            matrix[matrix_rows - 1][j] += matrix[matrix_rows][j + 1]
        j += 1
    matrix_rows -= 1

print(matrix[0][0])


