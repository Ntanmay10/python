# Write a program to find out whether the given name is present in the list or not

import os
os.system("cls")

name_list = ["Tanmay", "Chirag", "Deep", "yash"]

name = input("Enter your name: ")

if (name in name_list):
    print("Welcome to the partyyyy....")
else:
    print("Access denied")
