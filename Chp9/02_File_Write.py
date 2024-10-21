import os
os.system("cls")

quote = "Silence is the strongest tool that a man can possess"

f = open("Chp9/quote.txt", "w")
# If there is no such file then it will create one
f.write(quote)
f.close()
