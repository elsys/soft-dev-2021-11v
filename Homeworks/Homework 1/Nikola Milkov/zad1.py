import random

thislist = ["wardrobe", "microwave", "refrigerator", "purple", "pineapple", "spaghetti", "blueberry", "apricot", "vitamins", "table"]
word = random.choice(thislist)

correct = ""
fail = 6

for letter in word:
        if letter in correct:
            print(f"{letter}", end="")
        else:
            print("_ ", end="")
print("")
     
while fail > 0:
    guess = input("Enter a letter: ")

    if guess in word:
        print(f"Correct!")
    else:
        fail = fail - 1
        print(f"Incorrect! You have {fail} wrong guesses left!")
        
    correct = correct + guess
    wrong = 0
    
    for letter in word:
        if letter in correct:
            print(f"{letter}", end="")
        else:
            print("_ ", end="")
            wrong = wrong + 1
    print("")
     
    if wrong == 0:
        print(f"Congratulations! You guessed the word {word}!")
        break

else:
    print(f"You lost! The word was {word}!")
