# l = ["python","java","php","node","java",15,45.56,True]
# print(l)
# print(len(l))
# print(type(l))

# k = list((10,20,30,40))
# print(k)

#access list item
# l = [10,20,30,40,50,60]
# print(l[1])
# print(l[-1])
# print(l[1:5])
# print(l[1:5:2])
# print(l[-3:-1])
# print(l[::-1])

# print(10 in l)


#change list item
l = [10,20,30,40,50,60]

# l[2] = 500
# l[2:4] = [200,300,400]
# l.insert(0,500)
# l.append(800)
# k = ["a","b","c"]
# l.extend([100,200,300])
# l.extend(k)
# print(l)


# l.remove(10)
# l.pop()
# l.pop(1)
# l.clear()
# del l
# print(l)

# for i in l:
#     print(i)

# for i in range(len(l)):
#     print(l[i])

# i = 0
# while i<len(l):
#     print(l[i])
#     i+=1

# list cpmprehension

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# k = []
# for i in fruits:
#     if i.startswith("a"):
#         k.append(i)
# print(k)

# k = [i for i in fruits if i.startswith("a")]

# k = [i for i in fruits if "a" in i]

# k = ["abc" for i in fruits]
# print(k)


#sorting

l = [10,50,60,90,15,67]
l.sort()
# l.sort(reverse=True)
# l.reverse()
# k = sorted(l)
print(l)

# k = l
# k = l.copy()
# k = list(l)
# print(k)

# a = [10,20,30]
# b = [40,50,60]

# c = a+b
# a.extend(b)
# print(a)

# a = [10,20,30,40,50,10,10]
# print(a.count(20))
# print(a.index(20))