import os
os.system("cls")

age = int(input("Kaa umar hai tohri? "))

if (age <= 0):
    print("abe sathya gaye ho kaa??")
elif (age < 18):
    print("Tu bacha hai, homework ho gaya?")
else:
    print("Shadi ho gaya??")
