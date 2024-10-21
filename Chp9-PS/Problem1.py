# Write a program to read the text from given file "poems.txt" and fing out whether it contains the word "twinkle"

import os
os.system("cls")

with open("Chp9-PS/poems.txt") as p:
    content = p.read()
    if ("twinkle" in content.lower()):
        print("The poem consistes the required word")
    else:
        print("The poem does not consist of the required word")
