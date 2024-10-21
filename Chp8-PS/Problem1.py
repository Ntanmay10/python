# Write a program using function to find the greatest of three number

import os
os.system("cls")


def GOT(a, b, c):
    if (a > b and a > c):
        return a
    elif (b > a and b > c):
        return b
    else:
        return c


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

great = GOT(a, b, c)
# Output: The greatest of three
print("The greatest of three number is: ", great)
