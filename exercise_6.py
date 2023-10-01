# Iterate the given list of numbers and print only those numbers which are divisible by 5

def divisible_by_five(myList):
    print("Given list is: ", myList)
    print("Divisible by 5:")

    for number in myList:
        if(number % 5 == 0):
            print(number)

myList = [10, 20, 33, 46, 55]

divisible_by_five(myList)