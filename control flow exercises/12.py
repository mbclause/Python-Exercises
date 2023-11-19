'''
Find the factorial of a given number

Write a program to use the loop to find the factorial of a given number.

The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

For example: calculate the factorial of 5

5! = 5 x 4 x 3 x 2 x 1 = 120

Expected output:

120
'''

def factorial(num):
    result = 1

    for i in range(1, num + 1):
        result = result * i

    return result

result = factorial(5)



print(str(result))