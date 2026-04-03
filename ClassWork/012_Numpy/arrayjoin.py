import numpy as np

# a=np.array(
#         [
#             [
#                 [1,2],
#                 [3,4]
#             ],
#             [
#                 [5,6],
#                 [7,8]
#             ]
#         ]
# )
# b=np.array(
#         [
#             [
#                 [9,10],
#                 [11,12]
#             ],
#             [
#                 [5,6],
#                 [7,8]
#             ]
#         ]
# )
# k=np.concatenate((a,b))
# print(k)


# c=np.array([
#         [1,2],
#         [3,4]
# ])

# d=np.array([
#         [5,6],
#         [7,8]
# ])

# l=np.stack((c,d),axis=1)
# print(l)
# print(l.shape)




# a=np.array(
#         [
#             [
#                 [1,2],
#                 [3,4]
#             ],
#             [
#                 [5,6],
#                 [7,8]
#             ]
#         ]
# )
# b=np.array(
#         [
#             [
#                 [9,10],
#                 [11,12]
#             ],
#             [
#                 [5,6],
#                 [7,8]
#             ]
#         ]
# )

# m=np.stack((a,b))
# print(m)


# a = np.array([
#                [1,2,4],
#                [3,4,4],
#                [3,4,4]  ])
# b = np.array([ 
#                 [5,6,9],
#                 [7,8,7],  
#                 [7,8,7]]  )

# # k = np.concatenate((a,b))
# k = np.concatenate((a,b),axis=1)
# print(k)

# a = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# b = np.array([[[10,20],[30,40]],[[50,60],[70,80]]])

# k = np.concatenate((a,b),axis=2)
# print(k)


# a = np.array([10,20,30])
# b = np.array([30,40,60])

# # k = np.concatenate((a,b),axis=1)
# k = np.stack((a,b),axis=0)
# print(k.ndim)
# print(k)
