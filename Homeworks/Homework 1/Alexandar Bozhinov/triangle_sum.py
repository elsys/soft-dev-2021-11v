import random as random

sum = 0
maximum = 0

for i in range(1, 101):
    triangle = []
    for j in range(i):
        triangle.append(random.randint(0, 9))
    for j in triangle:
        if maximum < j:
            maximum = j
    sum += maximum

print("Maximum sum:", sum)