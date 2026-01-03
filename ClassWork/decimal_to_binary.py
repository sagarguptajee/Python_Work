# number=356
# st=0
# m=1

# while number !=0:
#     rem=number%2
#     # st=str(rem)+st
#     st=(rem*m)+st
#     number//=2
#     m*=10
# print(st)    



# decimal to octal
number=356
st=0
m=1

while number !=0:
    rem=number%8
    # st=str(rem)+st
    st=(rem*m)+st
    number//=8
    m*=10
print(st)    