# Calculate income tax for the given income by adhering to the rules below
# Taxable Income	Rate (in %)
# First $10,000	    0
# Next $10,000	    10
# The remaining	    20


def calc_tax(income):

    if(income > 20000):
        tax = 10000 * 0.1 + (income - 20000) * 0.2

    elif(income > 10000 and income <= 20000):
        tax = (income - 10000) * .1

    else:
        tax = 0

    return tax

tax1 = calc_tax(50000)

tax2 = calc_tax(19000)

tax3 = calc_tax(9000)

print(tax1)

print(tax2)

print(tax3)
