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



def mul(func):
    def ececute(*k):
        print(f"mul of {k[0]} and {k[1]} is ")



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