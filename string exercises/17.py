'''
Replace each special symbol with # in the following string

Given:

str1 = '/*Jon is @developer & musician!!'

Expected Output:

##Jon is #developer # musician##
'''

def replace_symbols(str):
    symbols = "/\!@#$%^&*()_-+='{''}'[]"
    for char in str:
        if char in symbols:
            str = str.replace(char, "#")

    return str

print("Given:\n/*Jon is @developer & musician!!")

print("Expected Output:\n", replace_symbols("/*Jon is @developer & musician!!"))