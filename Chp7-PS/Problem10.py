# Write a python program to print the multiplication table of n using for loop in reverse order

import os
os.system("cls")

n = int(input("Enter your number: "))

for i in range(1, 11):
    print(f"{n} * {11-i} = {n * (11-i)}")
