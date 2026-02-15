# class Animal:

#     def __init__(self,name,type):
#         self.name=name
#         self.type=type

#     def display(self):
#         print(self.name,self.type)


# class Dog(Animal):
    
#     def __init__(self, name, type,height,weight):
#         super().__init__(name, type)
#         self.height=height
#         self.weight=weight

#     def display(self):
#         print(self.name,self.type,self.height,self.weight)
#         super().display()



# class Cat(Animal):
#     pass

# d=Dog("tommy","husky",2,20)
# d.display()

# d1=Dog("jack","labra",3,30)
# d1.display()

# c=Cat("cilly","percian")
# c.display()


class mobile():

    def __init__(self,type,range):
        self.type=type
        self.range=range

    def display(self):
        print(self.type,self.range)


class vivo(mobile):

    def __init__(self, type, range,wifi,bluetooth):
        super().__init__(type, range)
        self.wifi=wifi
        self.bluetooth=bluetooth


    def display(self):
        print(self.type,self.range,self.wifi,self.bluetooth)


class oppo(vivo):
    pass

class iphone(vivo):
    
    def __init__(self, type, range, wifi, bluetooth,model):
        super().__init__(type, range, wifi, bluetooth)
        self.model=model


    def display(self):
        print(self.type,self.range,self.wifi,self.bluetooth,self.model)


o=oppo("Android",20000,"yes","yes")
o.display()

i=iphone("IOS",100000,"yes","yes","Iphone16")
i.display()
