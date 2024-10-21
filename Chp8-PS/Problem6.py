# Write a program that converts inches into cms

import os
os.system("cls")

def converter(inches):
    return inches * 2.54

inches = int(input("Enter inches: "))
print(f"{inches} inches is equal to {converter(inches)} cms") 
