# Write a program to accept a string from the user and display characters that are present at an even index number.

def even_chars(sentence):
    for i in range(len(sentence)):
        if(i % 2 == 0):
            print(sentence[i])

sentence = input("Enter a string: ")

even_chars(sentence)