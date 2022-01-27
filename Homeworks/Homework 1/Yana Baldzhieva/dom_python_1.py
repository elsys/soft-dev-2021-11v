import random

words = ["wwrd1", "wwrd2", "wwrd3", "wwrd4", "word5", "word6", "word7", "word8", "word9", "word10"]
rand_word = random.choice(words)

choice = 6
empty_word = []
for i in range(len(rand_word)):
    empty_word.append('_')

empty_word = ''.join(empty_word)

guess_word = list(empty_word)
while choice > 0:
    print(' '.join(guess_word))
    if ''.join(guess_word) == rand_word:
        print("Congrats, you have won!")
        break
    get_letter = input("Try: ")
  
    if get_letter in rand_word:
        print("Correct!") 
        for i in range(len(rand_word)):
            if list(rand_word)[i] == get_letter:
                    guess_word[i] = get_letter
        
    elif get_letter not in rand_word:
        print("Incorrect!")
        choice-=1
    
    if choice == 0:
        print("Sorry, you have lost")
        break
    




