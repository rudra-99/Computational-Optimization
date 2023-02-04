#Implementing the bracketing method for unimodular function
class bracket:
    def __init__(self):
        print('start:')
        self.low=int(input())
        self.high=int(input())
        self.number=int(input())
        self.delx=(self.high-self.low)/self.number 
        self.steps=0
        self.x1=self.low
        self.x2=self.x1+self.delx
        self.x3=self.x2+self.delx
    def check(self,x1,x2,x3):
        if self.func(x2)<self.func(x3) and self.func(x2)<self.func(x1):
            return True
        return False
     
    def func(self,x):
        if x==0:
            return None
        
        return ((x**2)+(54/x))
    def algorithm(self,x1,x2,x3):
        
        if self.check(x1,x2,x3)==True:
            print('The minimizer is : {} and the minimum cost obtained is: {}'.format(x2,self.func(x2)))
            self.steps+=1

        else:
            x1=x2
            x2=x3
            x3=x2+self.delx
            self.algorithm(x1,x2,x3)
            self.steps+=1

    def getPrecision(self):
        precision=2*(self.high-self.low)/self.number
        print('The precision of the range is {}'.format(precision))
    def get_number_of_steps(self):
        print('Number of steps required to complete the task is {}'.format(self.steps))

b=bracket()
b.algorithm(b.x1,b.x2,b.x3)
b.getPrecision()
b.get_number_of_steps()
