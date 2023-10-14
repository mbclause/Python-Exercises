# Print a downward Half-Pyramid Pattern of Star (asterisk)
# * * * * *  
# * * * *  
# * * *  
# * *  
# *

def print_pattern():
    i = 5

    while(i > 0):
        for j in range(i):
            print("*", end=' ')

        print("")
        i -= 1


print_pattern()
