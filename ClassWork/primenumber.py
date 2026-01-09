number =11
# flag = 0
for i in range(2,number):
    rem = number%i
    # print(i)
    if rem==0:
        # flag=1
        print(" Not prime")
        break
        
# if flag==0:
#     print("prime")
else:
    print("prime")
    