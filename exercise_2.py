# Write a program to iterate the first 10 numbers, 
# and in each iteration, print the sum of the current and previous number.


prevNum = 0

for i in range(10):
    sum = prevNum + i

    print("Current Number ", i, " Previous Number ", prevNum, " Sum: ", sum)

    prevNum = i