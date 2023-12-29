'''
Create an inner function to calculate the addition in the following way

    Create an outer function that will accept two parameters, a and b
    Create an inner function inside an outer function that will calculate the addition of a and b
    At last, an outer function will add 5 into addition and return it
'''

def add(a, b):
    def inner_add():
        return a + b
    
    res = inner_add()

    return res + 5


result = add(6, 7)

print(result)