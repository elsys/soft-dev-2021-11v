from pickle import TRUE
import random
list = ["aloda", "banan", "qbulka", "kon", "ovca", "stajprimilenkata", "milenkataetitan", "lubimiqtmiuchitel", "vulk", "axolotl"]
word = random.choice(list)

print("Hello!")
print("Wellcome to Hangman!")

letter = ""
flag = False
flag2 = True
remLetters = len(word)
arr = []


for i in range (len(word)):
    arr.append("_ ")

i = 0
m = len(word)

while i < 6:
    flag = False
    flag2 = False

    print(end = "\nYour word is: ")
    
    for j in range(len(arr)):
        print(end= arr[j])
    

    print("\nEnter a Letter: ")
    letter = input()

    for j in range (len(word)):
        if str(letter) == word[int(j)] and not (str(letter) == arr[j]):
            arr[j] = letter
            m -= 1
            flag = True
    if flag:
        if m == 0:
            print("\n\nCongratulations! \nYou won!")
            print("\nThe word is: " + word)
            exit()
        print("\nCorrect!")
        
    else:
        i += 1 
        if not(i == 6):
            print("\nTry again!\nYou have " + str(6-i) + " more lifes!")
        

print("\n\nSorry, you didn't guess the word!")
