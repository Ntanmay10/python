# A file contains the owrd Donkey multiple time
# Write a prgram to replace the word with ###

import os
os.system("cls")

word = "Donkey"

with open("Chp9-PS/donkey.txt") as d:
    content = d.read()


contentNew = content.replace(word, "######")

with open("Chp9-PS/donkey.txt", "w") as d:
    d.write(contentNew)
