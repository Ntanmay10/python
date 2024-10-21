# Write a program to accept marks of 6 students and store it in a sorted manner

import os
os.system("cls")

marks = []

stu1=int(input("Enter marks for student 1: "))
marks.append(stu1)
stu2=int(input("Enter marks for student 2: "))
marks.append(stu2)
stu3=int(input("Enter marks for student 3: "))
marks.append(stu3)
stu4=int(input("Enter marks for student 4: "))
marks.append(stu4)
stu5=int(input("Enter marks for student 5: "))
marks.append(stu5)
stu6=int(input("Enter marks for student 6: "))
marks.append(stu6)

marks.sort()
print(marks)