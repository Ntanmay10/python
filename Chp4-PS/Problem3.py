# Check that a tuple value cannot be changed in python

import os
os.system("cls")

a = (1, 10, 12, 18, 45, "Tanmay", "Chirag", "Deep", 93.0, False)
a[0] = 66 
# As tuples are immutable they cannot be changed
