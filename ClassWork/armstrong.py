# number=156
# temp=number
# sum=0

# while number !=0:
#     rem=number%10
#     sum+=(rem**3)
#     number=number//10


# if temp==sum:
#     print("armstromg")
# else:
#     print("not armstrong")    




for number in range(100,1000):
        temp=number
        sum=0
        while number !=0:
            rem=number%10
            sum+=(rem**3)
            number=number//10
        if temp==sum:
            print(f"{temp}armstromg")
        else:
            pass    