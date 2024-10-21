import os
os.system("cls")

quote = "\nStay hungry, stay foolish"

f = open("Chp9/quote.txt", "a")
# If there is no such file then it will create one
f.write(quote)
f.close()
