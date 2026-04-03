import pandas as pd
#Super store data load 
# order id , customer id delete 
# region and sales 

# dt=pd.read_csv("C:/Users/SAGAR GUPTA/Downloads/Superstore .csv",encoding='latin-1') 

# dt_copy=dt

# print(dt_copy.head())

# New_dt=dt_copy.drop(columns=['Order ID','Customer ID'],inplace=True) #inplace=true is delete from original file
# New_dt=dt_copy.drop(columns=['Order ID','Customer ID'])
# dt_copy.drop(['Order Id','Customer ID'],axis=1)

# print(New_dt.head())
# print(dt.head())


# viewdata=dt_copy[['Region','Sales']]
# print(viewdata)

# dt_copy.drop([0,2,4,6],axis=0,inplace=True)
# print(dt_copy.head())

dt=pd.read_csv("C:/Users/SAGAR GUPTA/Downloads/diamonds.csv")

Sel_row=dt[(dt['table']>=61)&(dt['cut']=="Ideal")]
# Sel_row=dt[(dt['table']>=65)|(dt['cut']=="Ideal")]
print(Sel_row)

