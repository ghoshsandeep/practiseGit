class myclass:
    
    def __init__(self,n1,n2):
        self.num1=n1
        self.num2=n2
        
    def SumNum(self):
        return self.num1 + self.num2
    


m1=myclass(4,5)
result=m1.SumNum()
print("the result is {0}".format(result)) 