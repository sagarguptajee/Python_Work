# f=open("test.txt",'w')
# f.write("Hello something")
# f.close()



# f=open("test.txt",'r')

# while True:
#     data=f.readline()
#     if "Hello" in data:
#         print(data)
#     if not data:
#         break

# f.close()


# f=open("test.txt",'r')

# while True:
#     data=f.readline()

#     if not len(data):
#         break
#     print(len(data))
# f.close()

with open("test.txt") as f:
    f.seek(10)
    print(f.tell())
    data=f.read()
    print(f.tell())
    print(data)
