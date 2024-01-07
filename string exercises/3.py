'''
Given two strings, s1 and s2, write a program to return a new string made of s1 and s2s first,
 middle, and last characters.

Given:

s1 = "America"
s2 = "Japan"

Expected Output:

AJrpan
'''

def blend_strings(s1, s2):
    mid1 = len(s1) // 2

    mid2 = len(s2) // 2

    s3 = s1[0] + s2[0] + s1[mid1] + s2[mid2] + s1[-1] + s2[-1]

    return s3

res = blend_strings("America", "Japan")

print(res)