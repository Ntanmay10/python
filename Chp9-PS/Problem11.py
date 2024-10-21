# Write a program to rename a file with renamed_by_python.txt

import os
os.system("cls")

with open("Chp9-PS/old.txt") as old:
    content = old.read()

with open("Chp9-PS/rename_by_python.txt", "w") as new:
    new.write(content)

file_path = "Chp9-PS/old.txt"
if os.path.isfile(file_path):
    os.remove(file_path)
    print(f"File '{file_path}' has been deleted.")
else:
    print(f"File '{file_path}' does not exist.")
