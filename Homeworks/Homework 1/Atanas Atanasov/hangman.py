import random

wordsToGuess = [
    'wolf',
    'main',
    'short',
    'long',
    'destruction',
    'building',
    'table',
    'plane',
    'apple'
]

def hangman():
    print("---------------------------------")

    fails = 0
    wordForGuessing = random.choice(wordsToGuess)
    guessedLetters = ''

    print('Nasko`s Hangman!')

    while fails != 6:
        win = True

        print(wordForGuessing[0], end = ' ')

        for i in range(1, len(wordForGuessing) - 1):
            if guessedLetters.find(wordForGuessing[i]) != -1:
                print(wordForGuessing[i], end = ' ')
            
            else:
                win = False
                print('_', end = ' ')

        if win == True:
            print('')
            print("---------------------------------")
            print(wordForGuessing)
            print('You won! Congratulations!')
            
            return None
        
        print(wordForGuessing[len(wordForGuessing) - 1])
        print('Number of guesses:', 6 - fails)
        print('Guess your letter:', end = ' ')

        userGuess = str(input())

        if guessedLetters.find(userGuess) != -1:
            print("---------------------------------")
            print('You have already tried that letter!')
            
            continue

        if len(userGuess) != 1 and (userGuess != ' ' or userGuess != '\n' or userGuess >= 'A' or userGuess <= 'Z') :
            print("---------------------------------")
            print('Invalid symbol')

            continue

        isIn = False
        
        for i in range(len(wordForGuessing)):
            if wordForGuessing[i] == userGuess:
                isIn = True

        print("---------------------------------")

        if isIn == False:
            print('Incorrect')
            fails += 1

        guessedLetters += userGuess

    print('Better luck next time')
        
hangman()