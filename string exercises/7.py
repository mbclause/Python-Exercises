'''
String characters balance Test

Write a program to check if two strings are balanced. For example, strings s1 and s2 
are balanced if all the characters in the s1 are present in s2. The characters position doesnt matter.

Given:

Case 1:

s1 = "Yn"
s2 = "PYnative"

Expected Output:

True

Case 2:

s1 = "Ynf"
s2 = "PYnative"

Expected Output:

False
'''

def check_balance(s1, s2):
    for char1 in s1:
        present = False

        for char2 in s2:
            if(char1 == char2):
                present = True

        if(present == False):
            return False
        
    return True


print(check_balance("Yn", "PYnative"))

print(check_balance("Ynf", "PYnative"))