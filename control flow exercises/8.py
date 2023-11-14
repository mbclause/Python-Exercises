'''
Print the following pattern

1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''

def print_pattern():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(i, end=' ')

        print()


print_pattern()