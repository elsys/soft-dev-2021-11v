from platform import java_ver
import random
import os

word_list = [
    'loser',
    'headache',
    'onion',
    'determine',
    'animals',
    'cruelty',
    'destruction',
    'fly',
    'system'
]

def Hangman():
    os.system('clear')
    word = random.choice(word_list)
    letter = ''

    error = 0

    print('Welcome, lets play Hangman!!!')

    while error != 6:
        you_won = True

        print(word[0], end = ' ')
        for i in range(1, len(word) - 1):
            if letter.find(word[i]) != -1:
                print(word[i], end = ' ')
            else:
                you_won = False
                print('_', end = ' ')

        if you_won:
            print('')
            os.system('clear')
            print(word)
            print('Congratulation for your win!!!')
            return None
        
        print(word[len(word) - 1])
        print('Tries remaining:', 6 - error)
        print('Guess one of the letters:', end = ' ')

        your_guess = str(input())

        if len(your_guess) != 1 and (your_guess != ' ' or your_guess != '\n' or your_guess >= 'A' or your_guess <= 'Z') :
            os.system('clear')
            print('Invalid symbol')
            continue

        if letter.find(your_guess) != -1:
            os.system('clear')
            print('The letter has been alwready used')
            continue

        symbol_present = False
        
        for i in range(len(word)):
            if word[i] == your_guess:
                symbol_present = True

        os.system('clear');
        if not symbol_present:
            print('Incorrect, try again!')
            error += 1

        letter += your_guess

    print('Next time is yours!!!')
Hangman()