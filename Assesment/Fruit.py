import json
dc={}

choice=int(input(""" WELCOME TO THE FRUIT MARKET 

                 1.MANAGER
                 2.CUSTOMER 

                 """))

if choice==1:

    cons='yes'

    while cons !='no':

        role=int(input("""Select Your Role:
                    
                    1.Add Fruits in Stocks
                    2.View stocks of Fruits
                    3.Update Stocks
                    

                    """ ))

        if role==1:

            def add_fruit():
                    name=input("Enter Fruit Name : ")
                    qyt=int(input("Enter Fruit Quantity : "))
                    price=int(input("Enter Fruit Price : "))
                    return name,qyt,price


            n=int(input("How many frouits you want to add?  : "))
            for i in range(n):
                    name,qyt,price=add_fruit()
                    try:
                     with open("fruits_data.json",'r') as f:
                         dc=json.load(f)
                    except:
                        dc={}
                    dc.update({name:{'quantity':qyt,'price':price}})

                    with open("fruits_data.json",'w') as f:
                         json.dump(dc,f)

        elif role==2:
            with open("fruits_data.json",'r') as f:
                 dc=json.load(f)
                 print(dc)

        elif role==3:
            def Update_fruit():
                name=input("Enter Fruit Name : ")

                if name in dc:
                        print("Fruit found:")
                        qyt=int(input("Enter Fruit Quantity : "))
                        price=int(input("Enter Fruit Price : "))
                        dc[name]['quantity']=qyt
                        dc[name]['price']=price
                        with open("fruits_data.json",'w') as f:
                             json.dump(dc,f,indent=5)
                        return name,qyt,price
                        
                else:
                    print(f"Fruit {name} is not available in stock")
            Update_fruit()  
        else:
            print("Invalid Choice you inputed")
        cons=input("Do you want to perform more operation? yes or no : ")

elif choice==2:
    temp='yes'
    last_order=None
    while temp !='no':
            token=int(input(""" WELCOME TO THE MARKET:
                        
                        1.PLACE ORDER
                        2.ORDER STATUS

                            """))
            try:
                with open("fruits_data.json",'r') as f:
                    dc=json.load(f)
            except:
                dc={}
            if token==1:
            
                    def place_order():
                                    name=input("Enter Fruit Name : ")
                                    qyt=int(input("Enter Fruit Quantity : "))
                                    return name,qyt
                    name,qyt=place_order()

                    if name in dc:
                        if dc[name]['quantity']>=qyt:
                            dc[name]['quantity']-=qyt
                            print("Order is placed succesfully")
                            last_order=name,qyt
                        else: 
                            print("not enough quantity:")
                    else:
                        print("Fruit is not in Stock")          
                    temp=input("Do you want to continue?yes or no : ")       
            elif token==2:
                
                try:
                   with open("fruits_data.json",'r') as f:
                       dc= json.load(f)  
                except:
                   dc={}   
                def order_status():
                    last_order
                    if last_order is not None:
                        name,qyt=last_order
                        print(f"""Your placed items are :
                              Fruit_Name={name}
                              Quantity={qyt}
                              Status_of_order=Dispatched        """)
                    else:
                        print("Order not placed yet")
                order_status()        
            else:
                print("invalid input")

else:
     print("invalid choice")
 

        


        