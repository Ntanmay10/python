# Write a program to find whether a given username is of less than 10 characters or not

import os
os.system("cls")

username = input("Enter your user name: ")

if (len(username) >= 10):
    print("Your username is greater than 10 characters")
else:
    print("Your username is less than 10 characters")
