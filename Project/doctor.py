time=[10,11,12,2,3]
db={}
import json

c='y'

while c !='n':

    choice=int(input("""Enter your choice :
                     
                     1.booking appointment
                     2.cancle appoinment
                     3.view all appointment

                     """))
    
    if choice==1:
        print("booking appointment:")
        name=input("Enter your Name :")
        phone=int(input("Enter your mobile No :"))

        Dr_Name=input("Enter doctor Name :")
        slot=int(input(f"enter slot:{time}"))

        if slot in time:
            k=[]
            for s in db.values():
                k.append(s['slot'])

            if slot in k:
                print("Appontment already taken")

            else:
                with open("data.json",'r') as f:
                    db=json.load(f)
                db.update({phone:{'name':name,'dr':Dr_Name,'slot':slot}})

                with open("data.json",'w') as f:
                    json.dump(db,f)
                    
        else:
            print("not avaliable for booking in this time slot")

    elif choice==2:
        print("cancle appointment:")
        phone=int(input("Enter Phone:"))

        db.pop(phone)
        print("Appointment Canclled")

    elif choice==3:
         with open("data.json",'r') as f:
                    data=json.load(f)
                    print(data)
        
    else:
        print("invalid choice:")

    c=input("do you want to continue?y or n :")

