import random

words = ["france", "italy", "scotland", "britain", "finland", "bulgaria", "norway", "austria", "switzerland", "iceland"]
word = random.choice(words)

game_word = list()
for i in range(len(word)):
    game_word.append('_')

print("Welcome to Hangman!")
mistakes = 0
while mistakes < 6:
    print(str(game_word))
    if game_word == list(word):
        print("You won!")
        break
    else:
        print("Guess your letter:")
        letter = input()
        if letter in word:
            for i in range(len(word)):
                if list(word)[i] == letter:
                    game_word[i] = letter
        else:
            print("Incorrect!")
            mistakes += 1

print("Your word was:")
print(word)