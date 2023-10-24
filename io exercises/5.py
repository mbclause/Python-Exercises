# Accept a list of 5 float numbers as an input from the user

myList = []

for i in range(5):
    num = input("enter a number: ")

    num = float(num)

    myList.append(num)

print(myList)