import random
import math

triangle = [
       3, 
      3, 4, 
     2, 4, 6, 
    8, 5, 1, 2,
   1, 7, 0, 6, 8
]

def generateTriangle(rows):
    list = []

    while rows > 0:
        for i in range(rows):
            list.append(random.randint(0, 10))
        rows -= 1

    return list    
        

combinations = []
ensResult = 0

def getSolution(layer = 0, index = 0):
    global ensResult
    solution = triangle[index]
    combinations.append(solution)

    if index + layer + 2 < len(triangle):
        solution = getSolution(layer + 1, index + layer + 1)
        if ensResult < sum(combinations):
            ensResult = sum(combinations)
        combinations.pop()

        solution = getSolution(layer + 1, index + layer + 2)
        if ensResult < sum(combinations):
            ensResult = sum(combinations)
        combinations.pop()

    return solution


getSolution()
print(ensResult)
triangle = generateTriangle(15)
getSolution()
print(ensResult)