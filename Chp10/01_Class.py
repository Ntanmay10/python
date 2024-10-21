import os
os.system("cls")


class Employee:
    language = "Python"
    salary = 250000


emp1 = Employee()
emp1.name = "Tanmay"
print(emp1.name, emp1.language, emp1.salary)

emp2 = Employee()
emp2.name = "Chixy"
print(emp2.name, emp2.language, emp2.salary)

# Here name is an instance/object attribute
# Salary and language are class attribute as they directly belong to the class
