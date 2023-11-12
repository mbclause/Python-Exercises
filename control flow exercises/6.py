# Print list in reverse order using a loop

def reverse_list(myList):
    myList = reversed(myList)

    for i in myList:
        print(i)

myList = [10, 20, 30, 40, 50]

reverse_list(myList)