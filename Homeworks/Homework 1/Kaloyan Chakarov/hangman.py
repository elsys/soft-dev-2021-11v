import random
import os

words = [
    'worker',
    'test',
    'opinion',
    'weather',
    'inflation',
    'wealth',
    'refrigerator',
    'management',
    'combination'
]

def game():
    os.system('clear')

    errors = 0
    word = random.choice(words)
    letters = ''

    print('Welcome to Hangman!')

    while errors != 6:
        won = True

        print(word[0], end = ' ')
        for i in range(1, len(word) - 1):
            if letters.find(word[i]) != -1:
                print(word[i], end = ' ')
            else:
                won = False
                print('_', end = ' ')

        if won:
            print('')
            os.system('clear')
            print(word)
            print('You won!')
            return None
        
        print(word[len(word) - 1])
        print('Number of guesses:', 6 - errors)
        print('Guess your letter:', end = ' ')

        guess = str(input())

        if len(guess) != 1 and (guess != ' ' or guess != '\n' or guess >= 'A' or guess <= 'Z') :
            os.system('clear')
            print('Invalid input')
            continue

        if letters.find(guess) != -1:
            os.system('clear')
            print('You have already tried that letter!')
            continue

        isThere = False
        
        for i in range(len(word)):
            if word[i] == guess:
                isThere = True

        os.system('clear');
        if not isThere:
            print('Incorrect')
            errors += 1

        letters += guess

    print('Next time champ!')
        
game()