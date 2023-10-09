# Write a program to check if the given number is a palindrome number.

def is_palindrome(number):
    original = number

    new_num = 0

    while number > 0:
        remainder = number % 10
        new_num = (new_num * 10) + remainder
        number = number // 10

    if (new_num == original):
        print("number is a palindrome")

    else:
        print("number is not a palindrome")


is_palindrome(12321)

is_palindrome(123)