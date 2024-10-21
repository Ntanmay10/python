# Write a program to find out whether a gien post is talking about Tanmay or not.

import os
os.system("cls")

word = "Tanmay"
post = input("Enter the ocntent of the post: ")

if word.lower() in post.lower():
    print("The post is talking about Tanmay")
else:
    print("The post doesn't resemble to Tanmay")
