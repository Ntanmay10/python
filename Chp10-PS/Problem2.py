# write a code to make a class "calculator" capable of finding square, cube, and square root of the given number

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


a = calculator(9)
a.square()
a.cube()
a.squareRoot()
