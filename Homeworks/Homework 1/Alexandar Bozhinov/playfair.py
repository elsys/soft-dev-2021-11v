playfair = ["T", "U", "E", "S", "A", 
            "B", "C", "D", "F", "G", 
            "H", "I", "K", "L", "M", 
            "N", "O", "P", "Q", "R", 
            "V", "W", "X", "Y", "Z"]    

print("Enter your message ( must be in capital letters ): ")
message = input()

collected = message.replace(" ", "")

divided = [collected[i:i+2] for i in range(0, len(collected), 2)]

x = 0
#for x in range(len(divided)):
#    if(divided[x][0] == divided[x][1]):
#        divided[x] = divided[1] + 'X' + divided[2]
#    elif(len(divided[x]) == 1):
#        divided[x] += "X"


print(*divided)