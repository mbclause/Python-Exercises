'''
Remove and add item in a list

Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.

Given:

list1 = [54, 44, 27, 79, 91, 41]

Expected Output:

List After removing element at index 4  [34, 54, 67, 89, 43, 94]
List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]
'''

def fourth_to_second(myList):
    item = myList[4]

    myList.remove(item)

    myList.insert(2, item)

    myList.append(item)

    return myList

list1 = [54, 44, 27, 79, 91, 41]

print("Given\n", list1)

print("output\n", fourth_to_second(list1))