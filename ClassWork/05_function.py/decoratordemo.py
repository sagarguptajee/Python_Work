# def before(fun):
#     def exe():
#         print("calling before test")
#         fun()
#         print("caling after test")
#     return exe

# @before
# def test():
#     print("test calling...")

# test()



# def add(func):
#     def execute(*k):
#         print(f"addition of {k[0]} and {k[1]} is {k[0]+k[1]}")
#         func(*k)
#     return execute


# def mul(func):
#     def execute(*k):
#         print(f"mul of {k[0]} and {k[1]} is {k[0]*k[1]}")
#         func(*k)
#     return execute


# @mul
# @add
# def calc(a,b):
#     pass

# calc(10,20)

def numcheck(fun):
    def exe(b):
        if b.isdigit():
            print("numeric number")

        else:
            print("invalid input")
        fun(b)
    return exe

def alphaheck(fun):
    def exe(c):
        if c.isalnum():
            print("alpha numaric")

        else:
            print("invalid input")
        fun(c)
    return exe


@numcheck
def check(a):
    pass
check("10")