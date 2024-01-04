'''
Create a string made of the first, middle and last character

Write a program to create a new string made of an input strings first, middle, and last character.

Given:

str1 = "James"

Expected Output:

Jms


'''


def chars(str):
    for i in range(len(str)):
        if i == 0:
            print(str[i], end='')

        if i == (len(str) // 2):
            print(str[i], end='')

        if i == len(str) - 1:
            print(str[i])

chars("James")