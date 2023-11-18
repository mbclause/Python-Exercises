'''
Use else block to display a message “Done” after successful execution of for loop

For example, the following loop will execute without any error.

Given:

for i in range(5):
    print(i)

Expected output:

0
1
2
3
4
Done!
'''

def print_loop(num):
    for i in range(num):
        print(i)
    else:
        print("Done")

print_loop(5)