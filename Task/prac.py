import numpy as np

arr1 = np.array([1, 2, 2, 3, 4])
arr2 = np.array([2, 2, 3, 3])

common = []

for x in arr1:
    if x in arr2:
        common.append(x)
        arr2 = np.delete(arr2, np.where(arr2 == x)[0][0])

print(common)