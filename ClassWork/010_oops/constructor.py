class Demo:

    def __init__(self,name,email):
        self.name=name
        self.email=email


    def display(self):
        print(self.name, self.email)

d=Demo("sagar","sagar@")
d.display()

d1=Demo("Hasan","Hasan@")
d1.display()
        