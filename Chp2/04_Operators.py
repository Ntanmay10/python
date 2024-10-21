# Arithmetic Operators
a = 1
b = 2
c = a+b
print(c)


# Assignment operators
d = 6-2  # assigns 4-2 in d
print(d)

e = 10
e += 5  # Increments the value of e by 5 and assign it to e
print(e)

f = 10
f -= 5  # Decrements the value of f by 5 and assign it to f
print(f)

g = 10
g *= 2  # Multiply the value of g by 2 and assign it to g
print(g)

h = 10
h /= 2  # Divide the value of h by 2 and assign it to h
print(h)


# Comparision operators (Always returns a boolean value)
i = 4 == 18
print(i)  # Prints False

j = 5 < 4
print(j)  # Prints False

k = 5 > 4
print(k)  # Prints True

l = 4 >= 4
print(l)  # Prints True

m = 4 <= 5
print(m)  # Prints True

n = 4 != 18
print(n)  # Prints True


# Logical Operators

# Truth table of 'or'
print("True or False is: ", True or False)
print("True or True is: ", True or True)
print("False or True is: ", False or True)
print("False or False is: ", False or False)

# Truth table of 'and'
print("True and False is: ", True and False)
print("True and True is: ", True and True)
print("False and True is: ", False and True)
print("False and False is: ", False and False)

# not operator
# Returns the inverted values of true and false
print(not (True))  # Prints False
print(not (False))  # Prints True
