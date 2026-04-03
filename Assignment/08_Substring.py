l1=[1,2,3,4,5]
l2=[3,4,5]

main_list=len(l1)
sub_list=len(l2)

result=False

for i in range(main_list-sub_list+1):
    if l1[i:i+sub_list]==l2:
        result=True
        break

if result:
    print("sub list is avalilable:")

else:
    print("not avaliable sub list")