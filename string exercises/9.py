'''
Reverse a given string

Given:

str1 = "PYnative"

Expected Output:

evitanYP
'''

def reverse_string(str):
    res = reversed(str)
    string = ""
    for char in res:
        string = string + char
    return string

print(reverse_string("PYnative"))