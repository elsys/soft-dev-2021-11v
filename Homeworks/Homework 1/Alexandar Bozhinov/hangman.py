print("Welcome to Hangman!")

words = ["PHONE", "MUSIC", "WATER", "CANDLE", "LAMP", "ELEPHANT", "FRIES", "SWEATSHIRT", "PLAYGROUND", "HOMEWORK"]

print("-------------------")

from pickle import FALSE, TRUE
import random
guess = random.choice(words)

str = []
correct = 0
x = 0
while x != len(guess):
    str.insert(x, "_")
    x += 1

def compareGuess(guess, str):
    z = 0
    same = 0
    for z in range(len(guess)):
        if(guess[z] == str[z]):
            same += 1
        z += 1
    if(same == len(guess)):
        return TRUE
    else:
        return FALSE

while correct < len(guess):
    if(compareGuess(guess, str) == TRUE):
        break
    print(*str)
    print("Guess your letter: ")
    letter = input()
    if(letter not in guess):
        print("Incorrect!")
    else:
        print("Cool! There is", letter, "in your word!")
        y = 0
        for y in range(len(guess)):
            if(letter == guess[y]):
                str[y] = letter
                correct += 1 
                if(letter in str):
                    correct -= 1
            y += 1   

print("Congratulations!")
print("Your word was", guess, "!")