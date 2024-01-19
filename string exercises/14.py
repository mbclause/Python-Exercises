'''
Remove empty strings from a list of strings

Given:

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

Expected Output:

Original list of sting
['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']

After removing empty strings
['Emma', 'Jon', 'Kelly', 'Eric']
'''

def remove_empty(myList):
    myList = filter(lambda n: not(n == "" or n == None), myList)

    return list(myList)

myList = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

print("Original List\n", myList)

myList = remove_empty(myList)

print("After removing empty strings\n", myList)