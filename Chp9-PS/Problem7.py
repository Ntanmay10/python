# write a program to find out the line number where the word is written in problem 6
import os
os.system("cls")

with open("Chp9-PS/log.txt") as l:
    lines = l.readlines()

lineNo = 1
for line in lines:
    if ("Python" in line):
        print(f"Python is written in line number {lineNo}")
        break
    lineNo += 1
else:
    print(f"No such word found")
