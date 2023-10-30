# Write a program to check if the given file is empty or not

import os

if(os.stat(r'C:\Users\brettoboe\Documents\GitHub\Python-Exercises\io exercises\test.txt').st_size > 0):
    print("file is not empty")

else:
    print("file is empty")