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
