# Write a program to find how many times substring “Emma” appears in the given string.

def count_tokens(sentence, token):
    sentence_list = sentence.split()

    return sentence_list.count(token)

str_x = "Emma is good developer. Emma is a writer"

print(count_tokens(str_x, "Emma"))

