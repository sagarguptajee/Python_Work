d = {"1":"sagar","3":"krushang","2":"hasan","70":"Amit"}
k = sorted(d.values())
u = {}

for l in k :
    for k,v in d.items():
        if v==l:
           u.update({k:v})

print(u)

# k = sorted(d.items(),key=lambda i : i[0])
# print(dict(k))