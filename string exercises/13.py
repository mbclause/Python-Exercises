'''
Write a program to split a given string on hyphens and display each substring.

Given:

str1 = Emma-is-a-data-scientist

Expected Output:

Displaying each substring

Emma
is
a
data
scientist
'''

def split(str):
    res = str.split("-")

    for item in res:
        print(item)

split("Emma-is-a-data-scientist")