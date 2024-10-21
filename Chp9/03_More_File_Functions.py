import os
os.system("cls")

f = open("Chp9/file.txt")

# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))

# line5 = f.readline()
# print(line5, type(line5))
# print(line5 == "")
# As we are not having line number 5 it will return an empty string

# lines = f.readlines()
# print(lines, type(lines))
# It will print all the lines in the file and the type will be list

line = f.readline()
while (line != ""):
    print(line)
    line = f.readline()

f.close()
