# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer

def exponent(base, exp):
    return pow(base, exp)

base = 2

exp = 3

result = exponent(base, exp)

print("2 to the power of 3 is ", result)