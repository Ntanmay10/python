# Write a program to find whether a given number is prime or not
import os
os.system("cls")

num = int(input("Enter your number: "))

for i in range(2, num):
    if (num % i) == 0:
        print("The number is not a prime number")
        break
else:
    print("The number is a prime number")
