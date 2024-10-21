# Write a program to find if a file is identical and have the same content as the other file

import os
os.system("cls")

with open("Chp9-PS/this.txt") as f1:
    content1 = f1.read()

with open("Chp9-PS/copy.txt") as f2:
    content2 = f2.read()


if content1 == content2:
    print("The content in both the file are same")
else:
    print("The files are diffrent at certain lines")
