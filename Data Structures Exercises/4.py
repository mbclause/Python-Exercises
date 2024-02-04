'''
Count the occurrence of each element from a list

Write a program to iterate a given list 
and count the occurrence of each element and create a dictionary to show the count of each element.

Given:

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

Expected Output:

Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}
'''

def count_occurence(myList):
    myDict = {}

    for item in myList:
        count = myList.count(item)

        myDict[item] = count

    return myDict

myList = [11, 45, 8, 11, 23, 45, 23, 45, 89]

myDict = count_occurence(myList)

print("List\n", myList)

print("Occurences of all list items\n", myDict)