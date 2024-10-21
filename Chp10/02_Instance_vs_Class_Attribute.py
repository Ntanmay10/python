import os
os.system("cls")


class Employee:
    language = "Python"
    salary = 250000


emp1 = Employee()
emp1.language = "JS"  # Instance attribute
print(emp1.language, emp1.salary)
