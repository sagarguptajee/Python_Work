# choice=int(input("Enter Choice:"))
# match choice:
#     case 1:
#         print("Gujarati")
#     case 2:
#         print("handi")
#     case 3:
#         print("English")
#     case _:
#         print("Invalid Choice")


num_1=int(input("please select first number:"))
num_2=int(input("please select second number:"))
choise=int(input(" Choice 1.add 2.sub 3.mul and 4.Div :"))

match choise:
    case 1:
        addition=num_1+num_2
        print(addition)
    case 2:
        subtraction=num_1-num_2
        print(subtraction)
    case 3:
        multi=num_1*num_2
        print(multi)
    case 4:
        divs=num_1/num_2
        print(divs)
    case _:
        print("Please enter valid Choice")    

