# # octaL to decimal 
# number=356
# st=0
# m=1

# while number !=0:
#     rem=number%10
#     # st=str(rem)+st
#     st=(rem*m)+st
#     number//=10
#     m*=8
# print(st)  


# BINARY to decimal
number=int(input("Enter your Binary number-"))
st=0
m=1

while number !=0:
    rem=number%10
    # st=str(rem)+st
    st=(rem*m)+st
    number//=10
    m*=2
print(st)  