# Write a python program to create a dictionary of hindi works with their values as english translations.
# Provide user an option to look it up

import os
os.system("cls")

words = {
    "sapota": "Chikoo",
    "Aam": "Mango",
    "Kela": "Banana",
    "Kaddu": "Pumpkin"
}

word = input("Enter the word to be translated: ")
print(f"The translation of {word} is:", words.get(word))
