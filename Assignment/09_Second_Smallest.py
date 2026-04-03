l1=[10,20,50,60,30,40,50,60,70]

filter_list=list(set(l1))
filter_list.sort()


if len(filter_list)>=2:
    sec_smallNo=filter_list[1]
    print("second smallest on list is: ",sec_smallNo)
else:
    print("Does not have sufficiant number in list, Required at least 3 list member")