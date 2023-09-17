#Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.


x = int(input("enter an integer: "))

y = int(input("enter another: "))

product = x * y

if(product <= 1000):
    print("Product = ", product)

else:
    print("Sum = ", x + y)




