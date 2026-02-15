class Calc:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self,obj):
        print(self)
        print(obj)
        return self.a+obj.a,self.b+obj.b

    # def __mul__(self,obj):
    #     return self.a*obj.a,self.b*obj.b


c1  =Calc(10,20)
c2 = Calc(40,50)

k = c1+c2
i = c1*c2
print(k)
print(i)