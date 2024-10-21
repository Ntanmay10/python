import os
os.system("cls")

a = 45
t = type(a)  # class <int>
print(t)  # will print <class int>

b = 45.5
t = type(b)  # class <float>
print(t)  # will print <class float>

c = "Tanmay"
t = type(c)  # class <String>
print(t)  # will print <class str>


# Type conversion
d = "45"  # Currently d is a string
e = int(d)  # Now the value of d is converted to integer
t = type(e)  # class <int>
print(t)  # will print <class int>
