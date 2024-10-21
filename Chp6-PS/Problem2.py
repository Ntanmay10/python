# Write a program to check whether a student is pass or fail
# It requires a total of 40% to pass
# And also minimun of 33% in each subject
# Take 3 subject input from user

import os
os.system("cls")

mark1 = int(input("Enter the marks of subject 1: "))
mark2 = int(input("Enter the marks of subject 2: "))
mark3 = int(input("Enter the marks of subject 3: "))

average = ((mark1+mark2+mark3)*100)/300

if (average >= 40 and mark1 >= 33 and mark2 >= 33 and mark3 >= 33):
    print("Mubarak hoo, sharmaji......")
else:
    print("Sharmaji ke bete ko dekha")
