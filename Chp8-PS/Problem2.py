# Write a program to convert celcius into faranhite using functions

import os
os.system("cls")


def converter(celc):
    faranhite = (celc*(9/5))+32
    return faranhite


celc = int(input("Enter the temperature: "))
print(f"The temperature is {celc} degree or {converter(celc)} faranhite")
