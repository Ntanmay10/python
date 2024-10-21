# create a class with class attribute a,
# create an onject from it and directly set obj.a = 0,
# Does this change class attribute

import os
os.system("cls")


class checkValue:
    a = 10


obj = checkValue()
print(obj.a)
# prints 10 (Class attribute) because the instance attribite is not present

obj.a = 0
print(obj.a)
# prints 0 becaus the instance attribiute is present

print(checkValue.a)
# prints 10 because the class attribite is called

# The class attribute is not changed by the instance attribute with the same name.
