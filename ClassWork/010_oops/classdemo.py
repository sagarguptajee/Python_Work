class pen:

    price=0
    company=""
    color=""

    def to_write(self):
        print(self.price,self.color,self.company)



p1=pen()
p1.price=500
p1.company="Cello"
p1.to_write()

p2=pen()
p2.price=700
p2.company="Renolds"
p2.to_write()

p3=pen()
p3.company="SS"
p3.to_write()