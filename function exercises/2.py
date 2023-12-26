'''
Write a program to create function func1() to 
accept a variable length of arguments and print their value.
'''

def func1(*args):
    for val in args:
        print(val)

func1(12)

func1(6, 7, 8)