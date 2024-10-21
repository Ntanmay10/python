# Write a python program to print the following pattern
'''
***
* *
***

for n = 3
'''

import os
os.system("cls")

n = int(input("Enter the number: "))

for i in range(1, n+1):
    if i == 1 or i == n:
        print("*" * n)
    else:
        print("*" + " " * (n-2) + "*")
