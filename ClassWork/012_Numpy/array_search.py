import numpy as np

# a = np.array([10,20,3,40,5,60])
# k = np.where(a%2==0)
# print(k)

# a = np.array(["python","java","php","anode","android"])
# # k = np.where()
# k = np.char.startswith(a,"a")
# print(np.where(k))


# a = np.array([10,20,3,40,5,60])
# a = np.array([[10,5],[4,9]])
# k = np.sort(a)
# print(k)


a = np.array([10,20,3,40,5,60])
k = a%2==0
b = a[k]
print(b)