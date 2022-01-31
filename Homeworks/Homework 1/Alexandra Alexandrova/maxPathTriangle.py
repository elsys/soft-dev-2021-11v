from random import randint

triangle = list()
i = 0
for i in range(1,6):
    numbers = list()
    j = 0
    while j < i:
        numbers.append(randint(0,9))
        j+=1
    triangle.append(numbers)

for row in range(len(triangle)-2, -1, -1):
    for col in range(len(triangle[row])):
        triangle[row][col] += max(triangle[row+1][col], triangle[row+1][col+1])

print(triangle[0][0])