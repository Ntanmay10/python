# The game() in python allows user to play game and returns score as integer.
# Read a file "Hi-Score.txt", which is either blank or contains previous high score.
# You need to write a program to update the high score whenever the game() breaks the previous high score

import os
import random
os.system("cls")


def game():
    print("You are playing a game...")
    score = random.randint(1, 50)

    # Fetch the high score
    with open("Chp9-PS/hiscore.txt") as h:
        hiscore = h.read()
        if (hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"your score is: {score}")
    if (score > hiscore):
        with open("CHp9-PS/hiscore.txt", "w") as h:
            h.write(str(score))
    return hiscore


game()
