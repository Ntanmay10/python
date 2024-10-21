# Write a program to print the multiplication table of given number using for loop

import os
os.system("cls")

num = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{num} * {i} = {num*i}")
