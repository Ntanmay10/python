# Write a python program to print the foloowing pattern
'''
*
**
***
'''

import os
os.system("cls")

n = int(input("Enter the number: "))

for i in range(1, n+1):
    print("*"*i)
