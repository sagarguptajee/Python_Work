import re

# k=re.match("Sun","Sun rises in east")
# k=re.search("s","Sun rises in east")
# k=re.findall("s","Sun rises in east")
# k=re.finditer("s","Sun rises in east")

# print(next(k)) #for finditer
# print(next(k))
# print(next(k))
# print(next(k))


# k=re.sub("s","X","Sun rises in east")
# print(k)

# k=re.split("s","sun rises in east")
# print(k)



# k=re.findall("p.t","Hel python ,pat Hello tops")
# k=re.search("^Hello","Hel python ,pat Hello tops")
# k=re.search("tops$","Hel python,pat Hello tops")

# k=re.search("He*l","Hal python,pat Hello tops")
# k=re.search("Hk+l","Hkkkkl python,pat Hello tops")
# k=re.search("Hk?l","Hl python,pat Hello tops")

# print(k)

# k=re.findall("[a-z0-9A-z]","Hello Python Hello Tops @ Hello world 121 121")
# k=re.findall("\d","Hello Python Hello Tops @ Hello world 121 121")
# k=re.findall("\D","Hello Python Hello Tops @ Hello world 121 121")
# k=re.findall("\w","Hello Python Hello Tops @ Hello world 121 121") #not allowed special char
# k=re.findall("\W","Hello Python Hello Tops @ Hello world 121 121")  # only special char
# k=re.findall("\S","Hello Python Hello Tops @ Hello world 121 121")
# k=re.findall("\s","Hello Python Hello Tops @ Hello world 121 121")
# print(k)

text="The certificate was issued"
k=re.search(r'\Bued',text)
print(k)


# k = re.search("\d{,10}","7485968574")
# print(k)


k = re.match("^[0-9]{10}$","7484404444")
print(k)

# email = input("enter email : ")
# k = re.match("^[a-zA-Z0-9_-]+@[a-zA-Z]+\\.[a-zA-Z]{2,4}$",email)
# if k is None : 
#     print("invalid email")
# else : 
#     print(email)




