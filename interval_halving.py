class intervalhalving:
    def __init__(self,low,high,epsilon):
        self.low=low
        self.high=high
        self.eps=epsilon
        self.xm=(self.high-self.low)/2
    def func(self,x):
        return ((x**2)+(54/x))
    def check(self,a,b):
        if abs(b-a)<self.eps:
            return True
        else:
            return False
    def findmin(self,x1,x2):
        
        self.l0=abs(self.high-self.low)
        x1=self.low+(self.l0/4)
        x2=self.high-(self.l0/4)
        
        if self.func(x1)<self.func(self.xm):
            self.high=self.xm
            self.xm=x1
            if self.check(self.low,self.high):
                print(f'The minimizer is {self.xm} and the minimum value obtained is {self.func(self.xm)}')
            else:
                self.findmin(x1,x2)
    
        else:
            self.low=self.xm
            self.xm=x2
           
            if self.check(self.low,self.high):
                print(f'The minimizer is {self.xm} and the minimum value obtained is {self.func(self.xm)}')
            else:
                self.findmin(x1,x2)
ih=intervalhalving(0,5,0.0001)
ih.findmin(None,None)
