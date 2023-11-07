# Calculate the sum of all numbers from 1 to a given number
def sum(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i

    print(sum)

num = int(input("enter a number: "))

sum(num)