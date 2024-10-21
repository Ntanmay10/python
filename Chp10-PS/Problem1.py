# Create a class programmer for storing details of few programmer working at microsoft

import os
os.system("cls")


class programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = programmer("Tanmay", 250000, 396360)
print(p.name, p.salary, p.company, p.pin)
r = programmer("Chixy", 200000, 396445)
print(r.name, r.salary, r.company, r.pin)
