# Create a new list from two list using the following condition
# Given two list of numbers, write a program to create a new list such that the new list should 
# contain odd numbers from the first list and even numbers from the second list.

def combine(list1, list2):
    newList = []

    for i, j in zip(list1, list2):
        if(i % 2 != 0):
            newList.append(i)

        if(j % 2 == 0):
            newList.append(j)

    newList.sort()

    return newList

list1 = [10, 20, 25, 30, 35]

list2 = [40, 45, 60, 75, 90]

result = combine(list1, list2)

print(result)