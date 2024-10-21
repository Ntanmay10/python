# A spam content is defined as a text containing following phrases:
# "making a lot of money"
# "buy now"
# "subscribe this"
# "click on the link"
# write a python program to detect the spam content

import os
os.system("cls")

p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click on the link"

message = input("Enter the message: ")

if (p1 in message or p2 in message or p3 in message or p4 in message):
    print("Abe baap ko matt sikha")
else:
    print("are vahhh, 25 din main paisa double")
