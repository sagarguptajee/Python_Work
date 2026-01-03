number=int(input("Enter your number:-"))

for i in  range(2,number):
    if number%i==0:
        print("not prime number")
        break
else:
     print("prime")    