'''
Calculate the sum and average of the digits present in a string

Given a string s1, write a program to return the sum and 
average of the digits that appear in the string, ignoring all other characters.

Given:

str1 = "PYnative29@#8496"

Expected Outcome:

Sum is: 38 Average is  6.333333333333333
'''

def sum_average(str):
    sum = 0

    count = 0

    for char in str:
        if char.isdigit():
            sum = sum + int(char)

            count += 1

    avg = sum / count

    print("Sum is: ", sum, " Average is: ", avg)


sum_average("PYnative29@#8496")