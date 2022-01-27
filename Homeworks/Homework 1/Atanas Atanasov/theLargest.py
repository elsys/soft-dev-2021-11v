import random
import math

triangle = [
       3, 
      7, 4, 
     2, 4, 6, 
    8, 5, 9, 3,
   1, 6, 0, 7, 8,
  2, 5, 6, 7, 7, 4
]

def generateTriangle(rows):
    list = []

    while rows > 0:
        for i in range(rows):
            list.append(random.randint(0, 10))
        rows -= 1

    return list    
        

possibleComb = []
outcome = 0

def getSolution(rows = 0, i = 0):
    global outcome
    result = triangle[i]
    possibleComb.append(result)

    if i + rows + 2 < len(triangle):
        result = getSolution(rows + 1, i + rows + 1)
        
        if outcome < sum(possibleComb):
            outcome = sum(possibleComb)
        
        possibleComb.pop()

        result = getSolution(rows + 1, i + rows + 2)
        
        if outcome < sum(possibleComb):
            outcome = sum(possibleComb)
        
        possibleComb.pop()

    return result


getSolution()
print(outcome)

triangle = generateTriangle(15)

getSolution()
print(outcome)