'''
Create a mixed String using the following rules

Given two strings, s1 and s2. Write a program to create a new string s3 made 
of the first char of s1, then the last char of s2, Next, the second char of s1 and 
second last char of s2, and so on. Any leftover chars go at the end of the result.

Given:

s1 = "Abc"
s2 = "Xyz..."

Expected Output:

AzbycX
'''

def combine_strings(s1, s2):
    s3 = ""
    for i in range(min(len(s1), len(s2))):
        s3 += s1[i] + s2[len(s2) - i - 1]

    if(len(s1) > len(s2)):
        s3 += s1[len(s2):]

    elif(len(s1) < len(s2)):
        s3 += s2[:len(s2) - len(s1)]

    return s3

print(combine_strings("Abc123", "Xyz"))