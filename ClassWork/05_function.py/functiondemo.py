# def get_msg():
#     print("hello")


# def sum(a,b):
#     print(f"sum of {a} and {b} is {a+b}")


# def square(a):
#     sq=a*a
#     return sq


# get_msg()
# sum(10,50)

# sq=square(5)
# print(sq)

# print(square(5))

# def total(a,b,c):
#     return a+b+c


# def per(a):
#     print((a*100)/150)


# t=total(35,35,35)
# per(t)

# def person(name,email="test",phone=0):
#     print(name,email,phone)


# person("keyu","keyu@gmail.com","7154646448")
# person("sagar")
# person("hasan",phone=97418465165)

# def sum(*a):
#     sum=0
#     for i in a:
#         sum+=i
#     print(sum)

# sum(10,20,30)


# def stu(**a):
#     print(a)

# stu(name="sagar",email="sagar@gmail")    

def square(a):
    return a*a

square=lambda a:a*a

print(square(10))