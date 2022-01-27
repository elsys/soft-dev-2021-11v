from random import randint

def generateTriangle():
    triangle = list()

    for row in range (1,100):
        helper = list()
        for number in range (0, row):
            helper.append(randint(0,9))
    
        triangle.append(helper)
    
    return triangle


def sumNums(triangle):
    for row in range(len(triangle) -2, -1, -1):
        for num in range (row):
            triangle[row-1][num] += max(triangle[row][num], triangle[row][num + 1])

    return triangle[0][0]


def main():
    triangle = list()
    triangle = generateTriangle()
    sum = sumNums(triangle)
    print(sum)

if __name__ == "__main__":
    main()
