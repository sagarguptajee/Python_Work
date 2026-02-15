class User:

    clg = "DRSTC"
    def __init__(self,name,email):
        self.name = name
        self.email = email

    @classmethod
    def test(cls,gender):
        print(gender)

    
    def display(self):
        print(self.name, self.email,self.clg)

    @staticmethod
    def abc():
        print("Hello")

# User.clg="abc"
# User.name = "hello"
# u = User("sagar","sagar@gmail.com")
# u.display()







# u1 = User("Keyu","keyu@gmail.com")
# u1.display()
# u1.abc()
User.test("male")
User.abc()

# class User:

#     clg="DRSTC"
    
#     def __init__(self,name,email):
#         self.name=name
#         self.email=email

#     def display(self):
#         print(self.name,self.email,self.clg)


# User.clg="abc"
# User.name="hello"
# u=User("sagar","sagar@")
# u.display()

# u1=User("keyu","keyu@")
# u1.display()