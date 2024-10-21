import os
os.system("cls")

'''
a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))
c = int(input("Enter the value of C: "))
avg = (a+b+c)/3
print("The average of the three numbers is: ", avg)

a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))
c = int(input("Enter the value of C: "))
avg = (a+b+c)/3
print("The average of the three numbers is: ", avg)

a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))
c = int(input("Enter the value of C: "))
avg = (a+b+c)/3
print("The average of the three numbers is: ", avg)
'''
# Instead of doing one same thing multiple times we can bind it inside a function


def average():
    a = int(input("Enter the value of A: "))
    b = int(input("Enter the value of B: "))
    c = int(input("Enter the value of C: "))

    avg = (a+b+c)/3
    print("The average of the three numbers is: ", avg)


average()
average()
average()
