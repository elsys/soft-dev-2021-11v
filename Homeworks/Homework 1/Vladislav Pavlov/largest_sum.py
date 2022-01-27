import random

def print_triangle(numbers):
    for i in range(len(numbers)):
        for j in numbers[i]:
            print(str(j) + " ", end="")
        print("")

def get_sum(numbers):
    for i in range(len(numbers)):
        for pos in range(len(numbers[-i-1])-1):
            if numbers[-i-1][pos] > numbers[-i-1][pos+1]:
                numbers[-i-2][pos]+=numbers[-i-1][pos]
            else:
                numbers[-i-2][pos]+=numbers[-i-1][pos+1]
    return numbers[0][0]

def fill_triangle(numbers, rows):
    n = 0;
    for i in range(rows):
        n+=1
        numbers.append([])
        for j in range(n):
            numbers[n-1].append(random.randint(0, 100))
            
rows = 100;
numbers = []
#numbers = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]


fill_triangle(numbers, rows)
print_triangle(numbers)
print(get_sum(numbers))