

user=int(input("Enter Number for series:"))

a=0 
b=1
print(a,b,end=" ")

for i in range(user):
    c=a+b
    print(c,end=" ")  #a=0,b=1,c=a+b=1,
    a=b
    b=c

