def factorial(n):
    if n < 0:
        print("Please input a number bigger than 0")
    elif n == 0:
        print("1")
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)


def divideRectangle(long, short):
    if long % short == 0:
        return short
    else:
        long, short = short, long % short
        return divideRectangle(long, short)


def my_sum(Lst):
    if len(Lst) == 0:
        return 0
    else:
        return Lst.pop(0) + my_sum(Lst)
