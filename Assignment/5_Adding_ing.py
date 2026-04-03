st=input("Emter your string value:")

if len(st)<3:
    add1=st
    print(add1)
elif st.endswith("ing"):
        add2=st+"ly"
        print(add2)
else:
    add3=st+"ing"
    print(add3)

    