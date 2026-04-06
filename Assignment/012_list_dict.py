l1=[(1,"a"),(2,"b"),(3,"c")]

dc={}

for key, values in l1:
    print('key=',key)
    print('values=',values)
    dc[key]=values

print(dc)   

# d=dict(l1)
# print(d)

