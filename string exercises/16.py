'''
Removal all characters from a string except integers

Given:

str1 = 'I am 25 years and 10 months old'

Expected Output:

2510
'''

def remove_non_ints(str):
    x = ""
    y = ""
    z = ""

    for char in str:
        if not(char.isdigit()):
            z = z + char

    myTable = str.maketrans(x, y, z)

    return str.translate(myTable)

print("Given:\nI am 25 years and 10 months old")

print("Expected Output:\n", remove_non_ints("I am 25 years and 10 months old"))