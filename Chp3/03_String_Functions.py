# The len() returns the length of the paramater
name = "Tanmay"
print(len(name))  # 6


# The endswith() returns True or False when checked and is also case sensative
print(name.endswith("y"))  # True
print(name.endswith("ay"))  # True
print(name.endswith("p"))  # False
print(name.endswith("ny"))  # False


# The startswith() returns True or False when checked and is also case sensative
print(name.startswith("T"))  # True
print(name.startswith("Tan"))  # False
print(name.startswith("t"))  # False
print(name.startswith("Taa"))  # False


# The capatalize() converts the first character of the string to capital letter
name2 = "tanmay"
print(name2.capitalize())  # Tanmay


# The count() counts the total number of occurances of the given value
print(name2.count("a"))  # 2


# The find() finds the given work and returns the first index of the occurance of the word
sentence = "Tanmay is a hero"
print(sentence.find("hero"))  # 12


# The replace()  replace all the occurances of the given value with the new value
print(sentence.replace("hero", "master"))  # Tanmay is a master
