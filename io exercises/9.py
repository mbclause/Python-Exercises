''' Format variables using a string.format() method.

Write a program to use string.format() method to format the following three variables as per the expected output

Given:

totalMoney = 1000
quantity = 3
price = 450

Expected Output:

I have 1000 dollars so I can buy 3 football for 450.00 dollars. '''

def format_strings():
    text = "I have {totalMoney} dollars so I can buy {quantity} footballs for {price:.2f} dollars."

    print(text.format(totalMoney = 1000, quantity = 3, price = 450))

format_strings()