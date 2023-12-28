'''
Create a function with a default argument

Write a program to create a function show_employee() using the following conditions.

    It should accept the employees name and salary and display both.
    If the salary is missing in the function call then assign default value 9000 to salary
'''

def show_employee(name, salary = 9000):
    print(name, salary)


show_employee("Ben", 12000)
show_employee("Jessa")