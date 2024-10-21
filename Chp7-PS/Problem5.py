# Write a program to find the sum of first n natural number using while loop

import os
os.system("cls")

num = int(input("Enter your number: "))

sum = 0
i = 1
while (i <= num):
    sum += i
    i += 1

print(sum)
