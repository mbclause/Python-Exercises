'''
Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

A recursive function is a function that calls itself again and again.

Expected Output:

55
'''

def recursive_sum(n):
    if n == 10:
        return n
    
    else:
        return n + recursive_sum(n + 1)
    

result = recursive_sum(0)

print(result)