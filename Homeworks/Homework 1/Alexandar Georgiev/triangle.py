from random import randint
from unittest import result

def creatingTriangle():
    n = 0
    matrix = []
    while n < 100:
        i = 0;
        col = []
        while i <= n:
            col.append(randint(0,10))
            i += 1
        n += 1
        matrix.append(col)
    return matrix   
def calculateTriangle():
    matrix = creatingTriangle()
    n = 0
    result = 0
    while n < 100:
        maxNumber = max(matrix[n])
        result += maxNumber
        n += 1
    return result

print(calculateTriangle())


