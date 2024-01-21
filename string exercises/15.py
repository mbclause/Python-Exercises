'''
Remove special symbols / punctuation from a string

Given:

str1 = "/*Jon is @developer & musician"

Expected Output:

"Jon is developer musician"
'''

def remove_symbols(str):
    x = ""
    y = ""
    z = ""

    for char in str:
        if not(char.isalnum()) and not(char == " "):
            z = z + char

    myTable = str.maketrans(x, y, z)

    return str.translate(myTable)

print("Given:\n/*Jon is @developer & musician")

print("Expected Output:\n", remove_symbols("/*Jon is @developer & musician"))