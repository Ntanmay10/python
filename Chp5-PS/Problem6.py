# Create an empty dictionary,
# allow 4 friends to enter their favourite language as key value pairs,
# assume that the names are unique

import os
os.system("cls")

d = {}

name1 = input("Enter friend 1 Name: ")
lang1 = input("Enter friend 1 language: ")
d.update({name1: lang1})

name2 = input("Enter friend 2 Name: ")
lang2 = input("Enter friend 2 language: ")
d.update({name2: lang2})

name3 = input("Enter friend 3 Name: ")
lang3 = input("Enter friend 3 language: ")
d.update({name3: lang3})

name4 = input("Enter friend 4 Name: ")
lang4 = input("Enter friend 4 language: ")
d.update({name4: lang4})

print(d)
