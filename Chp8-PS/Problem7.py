# Write a program using function to remove a word from the list and strip it at the same time

import os
os.system("cls")


def remover(l, word):
    n = []
    for item in l:
        if item != word:
            n.append(item.strip(word))

    return n


l = ["tanmay", "Chirag", "Deep", "Yash", "Meet"]
print(remover(l, "t"))
