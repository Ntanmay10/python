# Write a program to print the following pattern
'''
  *
 ***
*****
for n = 3
'''

import os
os.system("cls")

n = int(input("Enter the number: "))

for i in range(1, n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1), end="")
    print("")
