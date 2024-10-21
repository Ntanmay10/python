import os
import time
os.system("cls")


class Employee:
    language = "Python"
    salary = 250000

    def __init__(self, name, language, salary):
        # Its a dunder method which is automatically called when an object is created
        print("I am creating an object...")
        self.name = name
        self.language = language
        self.salary = salary

    def getInfo(self):
        print(f"The language is {
              self.language},\nand the slary is {self.salary}")

    @staticmethod  # Used when there are no dynamic values and hence we can avoid writing self paramater
    def greet():
        print("Hello, welcome to our company!")


emp1 = Employee("Tanmay", "JS", 300000)
print(emp1.name, emp1.salary, emp1.language)
emp1.getInfo()
