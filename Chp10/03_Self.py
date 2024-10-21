import os
os.system("cls")


class Employee:
    language = "Python"
    salary = 250000

    def getInfo(self):
        print(f"The language is {
              self.language},\nand the slary is {self.salary}")

    @staticmethod  # Used when there are no dynamic values and hence we can avoid writing self paramater
    def greet():
        print("Hello, welcome to our company!")


emp1 = Employee()
emp1.greet()
emp1.getInfo()
