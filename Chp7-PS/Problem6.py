# Write a program to find the factorial of the given number using for loop

import os
os.system("cls")

fact = 1
num = int(input("Enter your number: "))

for i in range(1, (num+1)):
    fact *= i

print(fact)
