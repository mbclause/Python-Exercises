'''
Create a string made of the middle three characters

Write a program to create a new string made of the middle three characters of an input string.

Given:

Case 1

str1 = "JhonDipPeta"

Output

Dip

Case 2

str2 = "JaSonAy"

Output

Son


'''

def middle_three(str):
    mid = len(str) // 2

    s = slice(mid - 1, mid + 2)

    return str[s]

print(middle_three("JhonDipPeta"))

print(middle_three("JaSonAy"))