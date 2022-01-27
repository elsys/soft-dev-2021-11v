from random import randint

def sum(p, m , n):
    for i in range(m - 2, -1, -1):
        for j in range(i + 1):
            if (p[i + 1][j] > p[i + 1][j + 1]):
                p[i][j] += p[i + 1][j]
            else:
                p[i][j] += p[i + 1][j + 1]
    return p[0][0]

pyramid = list()
j = input("enter matrix size ")
j = int(j)
for i in range (1, j):
    nums = list()
    k = 0
    while k < i:
        nums.append(randint(0, 9))
        k += 1
    pyramid.append(nums)

print(pyramid)
m = len(pyramid)
n = len(pyramid[0])
print(m)
print(n)
print(sum(pyramid, len(pyramid), len(pyramid[0])))