# Write a python program to print first n line in the following pattern
'''
n = 3
***
**
*
'''

import os
os.system("cls")


def pattern(n):
    if (n == 0):
        return
    print("*" * n)
    pattern(n - 1)


pattern(5)
