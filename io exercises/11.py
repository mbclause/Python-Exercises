# Read line number 4 from the file test2.txt

def read_line_4():
    fp = open(r'C:\Users\brettoboe\Documents\GitHub\Python-Exercises\io exercises\test2.txt', 'r')

    line_4 = ""

    for count, line in enumerate(fp, start=1):
        if(count == 4):
            line_4 = line

    print(line_4)


read_line_4()