'''
Count the total number of digits in a number
'''

def count_digits(num):
    count = 0

    while(num > 0):
        num = num // 10
        count +=1

    return count

print(count_digits(1001))

print(count_digits(19))

print(count_digits(1135345))