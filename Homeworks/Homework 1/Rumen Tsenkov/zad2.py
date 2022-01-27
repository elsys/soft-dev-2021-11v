import random
import math

triangle = [
       1, 
      9, 8, 
     1, 7, 6, 
    4, 50, 3, 3
]

def Triangle(symbols):
    list = []

    while symbols > 0:
        for i in range (symbols):
            list.append(random.randint(0, 10))
        symbols -= 1

    return list    
        

number_combinations = []
Result = 0

def Solution(row = 0, j = 0):
    global Result
    answer = triangle[j]
    number_combinations.append(answer)

    if j + row + 2 < len(triangle):
        answer = Solution(row + 1, j + row + 1)
        if Result < sum(number_combinations):
            Result = sum(number_combinations)
        number_combinations.pop()

        answer = Solution(row + 1, j + row + 2)
        if Result < sum(number_combinations):
            Result = sum(number_combinations)
        number_combinations.pop()

    return answer


triangle = Triangle(10)
Solution()
print('The answer is:')
print(Result)