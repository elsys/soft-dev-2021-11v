import random
# Yordan Markov N15 11v
# Math triangle

def math_triangle(numbers):
    sum = 0
    values = []
    for i in range(numbers + 1):
        values = []
        if i != 0:
            for j in range(i):
                values.append(random.randint(0, 9))
            for j in values: # Let's print the triangle
                print(f"{j} ", end = " ")
            print() # Separator
            max = 0
            for j in values:
                if max < j:
                    max = j
            sum += max
    print(f"Result: {sum}")

def main():
    # Triangle one - simple case:
    math_triangle(7)
    # Triangle two - complex case:
    math_triangle(100)

# Runs our main function
if __name__ == "__main__":
    main()