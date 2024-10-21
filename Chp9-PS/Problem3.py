# Write a program that generates multiplication table of 1-20.
# Write it into different files
# Place the files for a 13-year old

import os
os.system("cls")


def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n*i}\n"

    with open(f"Chp9-PS/Tables/table_{n}.txt", "w") as f:
        f.write(table)


for i in range(1, 21):
    generateTable(i)
