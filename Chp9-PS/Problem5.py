# Solve problem 4 with list other such censored words

import os
os.system("cls")

words = ["fuck", "asshole", "dick"]

with open("Chp9-PS/forprob5.txt") as f:
    content = f.read()


for word in words:
    content = content.replace(word, "#"*len(word))

with open("Chp9-PS/forprob5.txt", "w") as f:
    f.write(content)
