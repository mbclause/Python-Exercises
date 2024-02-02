'''
Slice list into 3 equal chunks and reverse each chunk

Given:

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

Expected Outcome:

Chunk  1 [11, 45, 8]
After reversing it  [8, 45, 11]
Chunk  2 [23, 14, 12]
After reversing it  [12, 14, 23]
Chunk  3 [78, 45, 89]
After reversing it  [89, 45, 78]
'''

def splice_reverse(myList):
    index = len(myList) // 3

    list1 = myList[0:index]

    list2 = myList[index:(index * 2)]

    list3 = myList[(index * 2):]

    list1 = list(reversed(list1))

    list2 = list(reversed(list2))

    list3 = list(reversed(list3))

    print("List1\n", list1)

    print("List2\n", list2)

    print("List3\n", list3)


original_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

print("Original list\n", original_list)

splice_reverse(original_list)