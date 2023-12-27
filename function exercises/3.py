'''
Write a program to create function calculation() such that it can accept 
two variables and calculate addition and subtraction. 
Also, it must return both addition and subtraction in a single return call.
'''

def calculation(val1, val2):
    add = val1 + val2

    sub = val1 - val2

    return add, sub

res = calculation(10, 7)

print(res)