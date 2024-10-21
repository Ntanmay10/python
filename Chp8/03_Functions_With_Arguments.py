import os
os.system("cls")


def greet(name, ending):
    print(f"Happy Diwali, {name}!")
    print(ending)

    return "This will be returned to a"


name = input("Enter your name: ")
os.system("cls")
greet(name, "have a good day")
greet("Chirag", "have a good day")
greet("Deep", "have a good day")

a = greet(1, 1)
print(a)
