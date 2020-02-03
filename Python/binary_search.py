# _*_ coding:utf-8 _*_


def binary_search(Lst, guess):
    low = 0
    high = len(Lst) - 1
    while low <= high:
        mid = (low + high) // 2
        item = Lst[mid]
        if guess == item:
            return mid
        elif guess < item:
            high = mid - 1
        else:
            low = mid + 1
    return None
