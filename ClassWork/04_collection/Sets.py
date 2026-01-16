# s = {10,20,30,40,50,60,60,True,1,False,0}

# s.add(1000)
# s.update({100,200})
# print(s)

# print(10 in s)

# a = {10,20,30,10}
# b = [100,200,300,100]
# a.update(b)
# print(a)

# b.extend(a)
# print(b)


s = {"java","python","node","php","android"}
# s.remove("java1")
# print(s)

# s.discard("java1")
# print(s)

# s.pop()

# s.clear()

# del s

# s = []
# s = ()
# s = set()
# print(s)
# print(type(s))

# for i in s:
#     print(i)


# a = {10,20,30,40,50,True}
# b = {40,50,60,70,80,1}

# a.update(b)
# c = a.union(b)
# c = a|b
# print(c)

# a.intersection_update(b)
# c  =a.intersection(b)
# c = a&b
# print(c)

# a.difference_update(b)
# c = a.difference(b)
# c = b-a
# print(c)

# a.symmetric_difference_update(b)
# c = a.symmetric_difference(b)
# c = a^b
# print(c)

# s = frozenset({10,20,30,40,50})
# print(s)

a = {10,20,30,40}
b = {100,200}
print(b.issubset(a))
print(a.issuperset(b))
print(a.isdisjoint(b))