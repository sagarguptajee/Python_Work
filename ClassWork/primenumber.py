number =17
flag = 0
for i in range(2,number):
    rem = number%i
    if rem==0:
        flag=1
        break
        
if flag==0:
    print("prime")
else:
    print("Not prime")