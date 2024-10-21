# Write a program using function to print the multiplication table of the given number

import os
os.system("cls")


def multi(n):
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")


n = int(input("Enter your number: "))
multi(n)
