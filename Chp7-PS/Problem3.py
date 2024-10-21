# Write a program to print the multiplication table of given number using while loop

import os
os.system("cls")

num = int(input("Enter your number: "))
i = 1
while (i < 11):
    print(f"{num} * {i} = {num*i}")
    i += 1
