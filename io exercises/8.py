# Accept any three string from one input() call

def three_strings():
    string1, string2, string3 = input("Enter three strings separated by a space: ").split()

    print(string1, string2, string3)


three_strings()