# Write a program to greet all person in the list whose name starts with s

import os
os.system("cls")

l = ["Tanmay", "Shivam", "Chirag", "Deep", "Satyam"]

for i in l:
    if i[0] == "S":
        print(f"Good Morning {i}")
