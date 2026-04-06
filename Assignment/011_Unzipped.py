k = ["1","2","3"]
j = ["A","B","C"]
i = ["X","Y","Z"]
d = zip(k,j,i)

# print(list(d))

for a,b,c in d:
    print(tuple(a,b,c))

k = zip(*d)
print(list(next(k)))
print(list(next(k)))
print(list(next(k)))


