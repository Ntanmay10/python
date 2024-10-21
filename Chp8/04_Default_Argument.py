import os
os.system("cls")


def greeting(name, ending="Thank you!!"):
    # if the value of ending is not supplied than it will print Thank you as default
    print(f"Good day, {name}")
    print(ending)


greeting("Tanmay")
