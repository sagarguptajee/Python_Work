import numpy as np

a=np.array(
        [
            [
                [1,2],
                [3,4]
            ],
            [
                [5,6],
                [7,8]
            ]
        ]
)

k=np.array_split(a,4)
print(k)

# a = np.array([10,20,30,40,50,60])
# k = np.array_split(a,3)
# print(k[1])


a = np.array([[10,20,30,78,70],[40,50,60,89,75]])
k = np.array_split(a,2,axis=1)
print(k)