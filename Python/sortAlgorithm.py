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



    


