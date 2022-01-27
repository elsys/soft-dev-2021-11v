import random

words = ["apple", "banana", "cherry", "march", "pen", "musical", "watch", "school", "window", "hacker", "phone", "mouse"]
word = random.choice(words)
guessed_letters = []
max_tries = 6
guessed = 0
   
print("Welcome to Hangman game\n")
print("This is your word\n")

while not guessed:
    
    for letter_guessed in word:
        if letter_guessed in guessed_letters:
            print(letter_guessed, end=" ")
        else:
            print("_", end=" ")
    print("\n")
    
    letter_guessed = input("Guess your letter: ")
    guessed_letters.append(letter_guessed)
    
    if letter_guessed in word:
        print("Correct!")

    if letter_guessed not in word:
        max_tries -= 1
        print("Incorrect!")
        if max_tries == 0:
            break
    
    guessed = 1
    
    for letter_guessed in word:
        if letter_guessed not in guessed_letters:
            guessed = 0

if guessed == 1:
    print("Congrats! You guessed the word! Your word was", word)
else: 
    print("Sorry! You did not guess the word! Your word was", word)


