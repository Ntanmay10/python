# Write a python code to fill in a letter template given below with name and date
letter = '''
    Dear <|Name|>,
    You are selected!
    <|Date|>
'''

print(letter.replace("<|Name|>", "Tanmay").replace("<|Date|>", "25 October"))
