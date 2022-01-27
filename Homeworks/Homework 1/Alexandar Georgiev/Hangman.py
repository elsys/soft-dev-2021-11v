
import random
def game():
    words = ("banana", "cherry", "apple", "python", "hangman", "mouse", "keyboard", "monitor", "laptop", "headphones")
    randomWord = random.choice(words)
    wrongChoices = 0
    wordList = []
    for x in randomWord:
        wordList.append("_")

    def winCheck(list):
        if "_" not in list:
            return 1
        elif wrongChoices == 6:
            return 1
        return 0
    while winCheck(wordList) == 0:
        print(wordList)
        userLetter = raw_input("Guess your letter: ")
        while len(userLetter) > 1 or len(userLetter) < 1:
            print("Incorrect letter, try inputing only one letter")
            userLetter = raw_input("Guess your letter: ")
        matchLetter = randomWord.find(userLetter)


        if matchLetter != -1:
            if randomWord.count(userLetter) != 0:
                while randomWord.count(userLetter) != 0:
                    wordList[matchLetter] = userLetter;
                    randomWord = list(randomWord)
                    randomWord[matchLetter] = "_"
                    new_string = ''.join(randomWord)
                    randomWord = new_string
                    matchLetter = randomWord.find(userLetter)
            else:
                wordList[matchLetter] = userLetter;

        else:
            print("Incorrect!")
            wrongChoices += 1
    if wrongChoices == 6:
        print("You ran out of tries")
    else:
        print("You win!")

    playAgain = raw_input("Do you want to play again? y/n: ")
    while playAgain != "y" or playAgain != "n":
        print("incorrect answer please type y(yes) or n(no)")
        playAgain = raw_input("Do you want to play again? y/n: ")
    if playAgain == "y":
        game()
    else:
        exit
print("Welcome to hangman!")
game()




    