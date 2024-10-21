import os
os.system("cls")

f = open("Chp9/file.txt")
print(f.read())
f.close()

# The same can be written with statement like this

with open("Chp9/file.txt") as f:
    print(f.read())
# With this we dont have to explicitly close the file
