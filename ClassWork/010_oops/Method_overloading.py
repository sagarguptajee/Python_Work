from multipledispatch import dispatch

class Calc : 

    @dispatch(int,int,int)
    def add(self,a,b,c):
        print(f"addition od {a} and {b} and {c} is {a+b+c}")
    
    @dispatch(int, int)
    def add(self,a,b):
        print(f"addition od {a} and {b} is {a+b}")





c=Calc()
c.add(10,20)
c.add(10,20,30)