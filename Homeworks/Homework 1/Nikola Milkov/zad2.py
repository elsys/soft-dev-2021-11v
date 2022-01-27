import random

rows = int(input("Enter Rows = "))

for i in range(1, rows + 1):
    for j in range(rows, i, -1):
        print(end = ' ')
    for k in range(1, i + 1):
        n = random.randint(1,9)
        print(n, end = ' ')
    print()
