# We all have played snake water gun in our childhood,
# if not then google the rules and write a program capable of playing this game with the user

'''
1 = snake
-1 = water
0 = gun
'''

import os
import random
os.system("cls")

computer = random.choice([-1, 0, 1])
youStr = input("Enter your choice: ")
youDict = {"s": 1,
           "w": -1,
           "g": 0}

you = youDict[youStr]
if (computer == you):
    print("It's a tie!")
else:
    if (computer == -1 and you == 1):
        print("Computer chose water, you chose snake. You win")
    elif (computer == -1 and you == 0):
        print("Computer chose water, you chose gun. You lose")
    elif (computer == 1 and you == -1):
        print("Computer chose snake, you chose water. Computer wins")
    elif (computer == 1 and you == 0):
        print("Computer chose snake, you chose gun, You win")
    elif (computer == 0 and you == -1):
        print("Computer chose gun, you chose water. Computer wins")
    elif (computer == 0 and you == 1):
        print("Computer chose gun, you chose snake, Computer wins")
    else:
        print("Something went wrong")
