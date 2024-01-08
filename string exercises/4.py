'''
Arrange string characters such that lowercase letters should come first

Given string contains a combination of the lower and upper case letters. 
Write a program to arrange the characters of a string so that all lowercase letters should come first.

Given:

str1 = PyNaTive

Expected Output:

yaivePNT
'''

def sort_case(str):
    lower = ""

    upper = ""

    for char in str:
        if(char.islower()):
            lower = lower + char

        else:
            upper = upper + char

    res = lower + upper

    return res

res = sort_case("PyNaTive")

print(res)