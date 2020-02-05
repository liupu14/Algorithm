def barrelSort(arr):
    Num = max(arr) + 1
    Lst = [0] * Num 
    for ii in arr:
        Lst[ii] += 1
    result = []
    for ii,item in enumerate(Lst):
        result = result + [ii] * item 
    return result 

def bubbleSort(Lst):
    Num = len(Lst)
    for ii in range(Num-1): 
        for jj in range(ii+1,Num): 
            if Lst[jj] < Lst[ii]:
                temp = Lst[ii]
                Lst[ii] = Lst[jj]
                Lst[jj] = temp 
    return Lst 

def bubbleSort2(Lst):
    Num = len(Lst)
    for ii in range(Numm-1):
        if Lst[ii] > Lst[ii+1]:
            Temp = Lst[ii]
            Lst[ii] = Lst[ii+1]
            Lst[ii+1] = Temp 
    return Lst 


def quicksort(Lst,left,right):
    if left < right:
        q = partial(Lst,left,right)
        quicksort(Lst,left,q-1)
        quicksort(Lst,q+1,right)

def partial(Lst,left,right):
    x = Lst[right]
    ii = left - 1
    for jj in range(left,right):
        if Lst[jj] <= x:
            Lst[ii],Lst[jj] = Lst[jj],Lst[ii]
    Lst[ii+1],Lst[right] = Lst[right],Lst[ii+1]
    return ii+1

def quicksort_recursive(Lst):
    if len(Lst) <= 1:
        return Lst 
    else: 
        pivot = Lst[0]
        litter = [ii for ii in Lst[1:] if ii <= pivot] 
        bigger = [ii for ii in Lst[1:] if ii  > pivot]
        return quicksort_recursive(litter) + [pivot] + quicksort_recursive(bigger)

def findSmallest(Lst):
    small = Lst[0]
    for ii,item in enumerate(Lst):
        if item <= small:
            small = item
            small_index = ii 
    return small_index 
            
def selectionSort(Lst):
    newarr = []
    for ii in range(len(Lst)):
        selection = findSmallest(Lst)
        newarr.append(Lst.pop(selection))
    return newarr
