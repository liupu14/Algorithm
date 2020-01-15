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

