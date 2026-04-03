import numpy as np

# a=np.array([
#             [
#             [11,22,33,44],
#             [1,2,3,4]
#             ]
#             ])

# b=np.array([[[5,6,7,8],
#             [55,66,77,88]]])

# k=np.concatenate((a,b),axis=2)

# print(k)


# a=np.array([[
#             [1,2,3,4]
#             ],
#             [
#                 [4,4,4,4]
#             ]   
#             ])
# b=np.array([
#         [
#     [5,6,7,8],
#         ] ,
#         [
#             [5,5,5,5]
#         ]
#           ])

# k=np.stack((a,b),axis=2)
# print(a.shape)
# print(k)
# print(k.shape)

a=np.array([[1,5,7],
            [9,8,7]])
b=np.array([
        [8,4,3],
        [5,9,1]
])

k=np.concatenate((a,b),axis=0)
print(k)

k=np.concatenate((a,b),axis=1)
print(k)

k=np.stack((a,b),axis=0)
print(k)

k=np.stack((a,b),axis=1)
print(k)