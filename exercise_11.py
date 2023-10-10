# Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

def extract_digits(num):
    while(num > 0):
        digit = num % 10

        print(digit, end = " ")

        num = num // 10


extract_digits(12345)