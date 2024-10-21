a = input("Enter number 1: ")
b = input("Enter number 2: ")
print("The value for a is:", a)  # lets assume 1
print("The value for b is:", b)  # lets assume 34
# Here it will return 134 because by default input function scan everything as a string
print("The sum is:", a+b)

# Solution
c = int(input("Enter number 1: "))
d = int(input("Enter number 2: "))
print("The value for c is:", c)  # lets assume 1
print("The value for d is:", d)  # lets assume 3
# Here it will return 4 as we have converted the values to integer value
print("The sum is:", c+d)
