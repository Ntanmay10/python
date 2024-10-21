# Write a proram to mine a log file and find whether it contains 'python'

import os
os.system("cls")

word = "python"

with open("Chp9-PS/log.txt") as l:
    content = l.read()
    if word in content.lower():
        print(f"Found {word} in the log file")
    else:
        print(f"Can't find {word} in the lof file")
