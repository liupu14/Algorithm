class sortAlgorithm():
   
    def __init__(self,L):
        self.L = L
    
    def barrelSort(self):
        Num = max(self.L) + 1
        Lst = [0] * Num 
        for ii in self.L:
            Lst[ii] += 1
        result = []
        for ii,item in enumerate(Lst):
            result = result + [ii] * item 
        return result 

    def bubbleSort(self):
        Num = len(self.L)
        for ii in range(Num-1):
            for jj in range(ii+1,Num):
                if self.L[jj] < self.L[ii]:
                    temp = self.L[ii]
                    self.L[ii] = self.L[jj]
                    self.L[jj] = temp 
        return self.L 

    def bubbleSort2(self):
        Num = len(self.L)
        for ii in range(Numm-1):
            if self.L[ii] > self.L[ii+1]:
                Temp = self.L[ii]
                self.L[ii] = self.L[ii+1]
                self.L[ii+1] = Temp 
        return self.L 


    def quicksort(self,left,right):
        if left < right:
            q = sortAlgorithm.partial(self.L,left,right)
            quicksort(self.L,left,q-1)
            quicksort(self.L,q+1,right)

    def partial(self,left,right):
        x = self.L[right]
        ii = left - 1
        for jj in range(left,right):
            if self.L[jj] <= x:
                self.L[ii],self.L[jj] = self.L[jj],self.L[ii]
        self.L[ii+1],self.L[right] = self.L[right],self.L[ii+1]
        return ii+1
