
list1=[1, 1, 1, 5,5, 3, 1, 3, 3, 1,4, 4, 4, 2, 2, 2, 2]

# for i in set(list1):
#     print(f"{i}:{list1.count(i)}", end=" ")

    


dic={}
for i in list1:
    if i in dic:
     dic[i]+=1
    else:
       dic[i]=1

print(dic)       

    