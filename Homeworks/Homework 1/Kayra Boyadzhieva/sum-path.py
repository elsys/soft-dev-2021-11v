import random

n = 5
numbers = []
sum=0

for i in range(n + 1):
    numbers = []
    for j in range(i):
        numbers.append(random.randint(0, 9))
    for j in numbers: 
        print(j, end = " ")
    print("\r")

    max_num = 0
    for j in numbers:
        if j>max_num:
            max_num=j
    sum = sum + max_num

print("The maximum sum of the path is", sum)

