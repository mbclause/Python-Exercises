'''
Create a list by picking an odd-index items from the first list and even index items from the second

Given two lists, l1 and l2, write a program to create a third list l3 by 
picking an odd-index element from the list l1 and even index elements from the list l2.

Given:

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

Expected Output:

Element at odd-index positions from list one
[6, 12, 18]
Element at even-index positions from list two
[4, 12, 20, 28]

Printing Final third list
[6, 12, 18, 4, 12, 20, 28]
'''

def odd_even_list(list1, list2):
    list3 = list1[1::2] + list2[::2]

    return list3


list1 = [3, 6, 9, 12, 15, 18, 21]

list2 = [4, 8, 12, 16, 20, 24, 28]

list3 = odd_even_list(list1, list2)

print("Given:\n", list1, "\n", list2)

print("Combined lists\n", list3)