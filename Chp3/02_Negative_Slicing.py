name = "Tanmay"

neg_slice = name[-6:-3]  # This will work in the same manner as below example:
print(neg_slice)
pos_slice = name[0:3]  # Is same as the abover example
print(pos_slice)

# Other random example
print(name[:5])
# This will print all the characters from 0 all the way to 5 index, If we dont assing the end point it will have 0 by default
print(name[0:])
# This will print all the characters from 0 all the way to -1 index, If we dont assing the end point it will have -1 by default


# Skip Slicing
# This will print every 2nd character (tna will br printed)
print(name[0:-1:2])
print(name[1:-1:2])  # This will print every 2nd character (am will beprinted)
