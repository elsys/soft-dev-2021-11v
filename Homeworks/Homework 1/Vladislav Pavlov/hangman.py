import random

word_list = ["word1", "hello", "world", "zdravei", "problem", "shrek", "purification", "eighthword", "frankenstein", "abracadracadabra"]
wrong_answers = 0
word = word_list[random.randint(0, 9)]
current_board = list(len(word)*"_")

print("Welcome to hangman!")

while(wrong_answers < 6 and "_" in current_board):
    print("".join(current_board) + "\n")
    inpt = input("Guess your letter: ")
    if(len(inpt) != 1):
        print("invalid input")
        continue
    inpt = inpt.lower()
    if(inpt in word):
        for pos,char in enumerate(word):
            if(inpt == char):
                current_board[pos] = inpt
    else:
        print("Incorrect!")
        wrong_answers += 1

if(wrong_answers > 5):
    print("Game Over! You lost!")
else:
    print("Conratulations! You won!")
