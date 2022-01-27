import random 

def get_word():
    words = ["alligator", "deer", "panda", "camel", "horse", "sheep", "giraffe", "python", "duck", "elephant"]
    random_word = random.choice(words)
    print(random_word)
    return random_word.upper()


def game(word):
    letters = list("_" * len(word))
    choice = 6
    correct = 1
    counter = 0

    print ("Welcome to Hangman!")
    while choice > 0 :
        if (correct == 1):

            for i in range(len(word)):
                print(letters[i], end =" ")   
    
            print("\n")

        letter = input("Guess your letter: ").upper()
        correct = 0
        counter = 0

        for i in range(len(word)):
            if (word[i].upper() == letter):
                letters[i] = letter
                correct = 1
            
            if (letters[i] != "_"):
                counter+=1

        if (counter == len(letters)):
            return correct

        if (correct == 0):
            print("Incorrect!")
            choice-= 1


def main():
    word = get_word()
    check = game(word)

    if (check == 1):
        print("\nEnd game! You win!")
    else:
        print("\nEnd game! You lose!")


if __name__ == "__main__":
    main()
