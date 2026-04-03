# l=(10,20,30,40,50)
# k=iter(l)

# print(next(k))
# print("hello")
# print(next(k))

def square(a):
    for i in range(a):
        yield i*i
a=iter(square(10))
print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))