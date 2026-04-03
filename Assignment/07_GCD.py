no_1=int(input("enter your first number:"))
no_2=int(input("enter your second number:"))

for i in range(1,no_1+1):
    if no_1%i==0:
        print(list(i))

for j in range(1,no_1+1):
    if no_2%j==0:
        print(list(j))

