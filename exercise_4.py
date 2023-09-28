#Write a program to remove characters from a string starting from zero up to n and return a new string.

import sys

word = input("enter a string: ")

print("Enter a number less than ", len(word))

n = int(input())

while(n >= len(word)):
    print("Enter a number less than ", len(word))

    n = int(input())

newWord = word[n:]

print(newWord)
