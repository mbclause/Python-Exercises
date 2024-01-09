'''
Count all letters, digits, and special symbols from a given string

Given:

str1 = "P@#yn26at^&i5ve"

Expected Outcome:

Total counts of chars, digits, and symbols 

Chars = 8 
Digits = 3 
Symbol = 4
'''

def count_symbols(str):
    chars = 0

    digits = 0

    symbols = 0

    for char in str:
        if char.isalpha():
            chars += 1

        elif char.isdigit():
            digits += 1

        elif not(char.isalpha()) and not(char.isdigit()):
            symbols += 1

    print("Chars = ", chars)

    print("Digits = ", digits)

    print("Symbols = ", symbols)


count_symbols("P@#yn26at^&i5ve")