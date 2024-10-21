# Write a program to make a copy of the file named "this.txt"

import os
os.system("cls")

with open("Chp9-PS/this.txt") as org:
    contCpy = org.read()

with open("Chp9-PS/copy.txt", "w") as cpy:
    cpy.write(contCpy)
