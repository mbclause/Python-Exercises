'''
Write a program to count occurrences of all characters within a string

Given:

str1 = "Apple"

Expected Outcome:

{'A': 1, 'p': 2, 'l': 1, 'e': 1}
'''

def count_chars(str):
    characters = ({})
    for char in str:
        num = str.count(char)
        if not(char in characters):
            characters[char] = num


    return characters


print(count_chars("Apple"))