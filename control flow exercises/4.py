'''
Display numbers from a list using loop

Write a program to display only those numbers from a list that satisfy the following conditions

    The number must be divisible by five
    If the number is greater than 150, then skip it and move to the next number
    If the number is greater than 500, then stop the loop
'''

def print_list(myList):
    for item in myList:
        if(item > 500):
            return

        if(item % 5 == 0):
            if(item > 150):
                continue
            else:
                print(item)

myList = [75, 2, -25, 200, 16, 0, 501, 25]

print_list(myList)