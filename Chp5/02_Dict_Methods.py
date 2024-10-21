import os
os.system("cls")

marks = {
    "Tanmay": 96,
    "Chirag": 82,
    "Deep": 78,
    58: "Tanmay"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Tanmay": 98, "Yash": 72})
# print(marks)

print(marks.get("Mali"))
# print(marks["Mali"])
# The difference between the above two statement is that if the value dosent exists then the get method will return None,
# while the Line No. 18 will return an error
