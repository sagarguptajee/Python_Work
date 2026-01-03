
# for i in range(2,101):
#     # print(i)
#     for j in range(2,i):
#         if i%j==0:
#             print(i,"not prime")
#             break
#     else:
#         print(i,"prime")




for i in range(2,101):
    # print(i)
    for j in range(2,i):
        if i%j==0:
            # print(i,"not prime")
            break
    else:
        print(i,"prime")
