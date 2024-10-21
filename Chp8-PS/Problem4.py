# Write a recursive function to find the sum of first n natural number

import os
os.system("cls")


def _sum(n):
    if (n == 1):
        return 1
    return _sum(n - 1) + n


num = int(input("Enter the number: "))
print(f"The sum of 1 to {num} is {_sum(num)}")
