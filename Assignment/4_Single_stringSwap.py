st1=input("Enter Your First String:")
st2=input("Enter Your Second String:")

if len(st1)<2 or len(st2)<2:
    print("Minimum two Charater reqired for it")
else:
     word1=st2[:2]+st1[2:]
     word2=st1[:2]+st2[2:]
     addition=word1+" "+word2
     print("Addion of two swap string is:",addition)
    
