# Write all content of a given file into a new file by skipping line number 5

def change_file():
    lines = []

    fp = open(r'C:\Users\brettoboe\Documents\GitHub\Python-Exercises\io exercises\test.txt', 'r')

    lines = fp.readlines()
    
    fp2 = open(r'C:\Users\brettoboe\Documents\GitHub\Python-Exercises\io exercises\output.txt', 'w')

    counter = 1

    for line in lines:
        if(counter % 5 != 0):
            fp2.write(line)
    
        counter += 1


change_file()