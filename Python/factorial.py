def factorial(x):
    if x == 1:
        return 1
    else:
        return factorial(x-1) * x

X = int(input("Please enter a interge:"))
print(factorial(X))
