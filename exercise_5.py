# Write a function to return True if the first and last number of a given list is same. 
# If numbers are different then return False.

def first_last(myList):
    if(myList[0] == myList[-1]):
        return True
    
    else:
        return False
    

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

print("Given list ", numbers_x, " the result is: ", first_last(numbers_x))

print("Given list ", numbers_y, " the result is: ", first_last(numbers_y))