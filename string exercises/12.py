'''
Find the last position of a given substring

Write a program to find the last position of a substring “Emma” in a given string.

Given:

str1 = "Emma is a data scientist who knows Python. Emma works at google."

Expected Output:

Last occurrence of Emma starts at index 43
'''

str = "Emma is a data scientist who knows Python. Emma works at google."

token = "Emma"

print("Last occurrence of ", token, " starts at index ", str.rfind(token))