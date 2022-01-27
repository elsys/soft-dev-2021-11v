import random
# Yordan Markov N15 11v
# Hangman

def Hangman(word):
    list_of_letters = list(word)
    list_of_letters = ' '.join(list_of_letters)
    guessing = []
    for i in range (len(word)):
        guessing.append('_')
    guessing = ' '.join(guessing)
    guess_counter = 0
    already_guessed = []
    did_we_guess = list(word)
    did_we_guess = ' '.join(did_we_guess)
    while True:
        print(guessing)
        flag = 0
        guess = "Go to \"While\"" # In order to go to the "While" clause, "guess" should be initialized.
        while (len(guess)) > 1 or (len(guess)) < 1 or flag == 1:
            flag = 0
            guess = input("Your guess: ")
            if guess.upper() in already_guessed:
                print("You have already guessed that letter!")
                flag = 1
        if (guess.upper() in list_of_letters or guess.lower() in list_of_letters) and guess.upper() not in already_guessed:
            # do something
            print("Correct!")
            for i in range(len(list(list_of_letters))):
                did_we_guess = list(word)
                if list_of_letters[i] == guess.upper() or list_of_letters[i] == guess.lower():
                    guessing = list(guessing)
                    guessing[i] = guess.upper()
                    guessing = ''.join(guessing)
                    already_guessed.append(guess.upper())
                did_we_guess = ''.join(did_we_guess) # Back to string
        else:
            flag = 1
        if flag == 1:
            guess_counter += 1
            print(f"Incorrect!\nRemaining tries: {6 - guess_counter}")
        if guess_counter == 6:
            print(f"You lost.\nThe word was: {word}\nGood game!")
            break
        if guessing == list_of_letters.upper():
            print(f"You won!\nThe word was: {word}\nGood game!")
            break

def main():
    list_of_words = ["Cat", "Transmitter", "Milk", "Globe", "Piano"]
    word = random.choice(list_of_words)
    Hangman(word) # Let's play Hangman!

# Runs our main function
if __name__ == "__main__":
    main()