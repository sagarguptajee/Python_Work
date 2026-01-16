# n = 10

# a, b = 0, 1
# print("Fibonacci Series:")

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b
    

a=0
b=1
print(a,b,end=" ")

for i in range(10):
    c=a+b
    print(c,end=" ")
    a=b
    b=c