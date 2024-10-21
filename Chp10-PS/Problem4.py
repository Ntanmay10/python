# Add a static method in problem 2 to greet user with hello

import os
os.system("cls")


class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"Square of {self.n} is {self.n*self.n}")

    def cube(self):
        print(f"Cube of {self.n} is {self.n*self.n*self.n}")

    def squareRoot(self):
        print(f"Square Root of {self.n} is {self.n**1/2}")

    @staticmethod
    def hello():
        print("Hello User")


a = calculator(9)
a.hello()
a.square()
a.cube()
a.squareRoot()
