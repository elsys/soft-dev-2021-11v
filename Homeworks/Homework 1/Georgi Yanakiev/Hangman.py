import random 

word = ["Zdarova", "Breitan", "Duma", "dadfjsdifgjsdjiof"]
print ("Welcome to Hangman!")
num = random.randint(0, 3)
isFull = False
correct_guesses = ""
wrong_answers = 0
print("_ " * len(word[num]))



while wrong_answers < 6 and isFull == False :
    guess = input("\nGuess your letter:")
    isFull = True

    if len(guess) > 1:
        print("Incorrect!")
        continue

    if guess in word[num]:
        correct_guesses += guess
        for letter in word[num]:
            if letter in correct_guesses:
                print(letter, "", end = "")
            else:
                isFull = False
                print("_ ", end = "")

    else:
        wrong_answers += 1
        print("Incorrect!")

if wrong_answers > 5:
    print("You failed")
else:
    print("You won")

