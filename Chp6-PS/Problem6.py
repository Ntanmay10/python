# Write a program to calculate the marks of the student and give grades accordingly:
# 90-100 => Ex
# 80-90 => A
# 70-80 => B
# 60-70 => C
# 50-60 => D
# <50 => E

import os
os.system("cls")

marks = int(input("Enter your marks: "))

if (marks > 90):
    print("Excellent")
elif (marks > 80):
    print("A")
elif (marks > 70):
    print("B")
elif (marks > 60):
    print("C")
elif (marks > 50):
    print("D")
else:
    print("E")
