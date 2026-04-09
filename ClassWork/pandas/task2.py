import pandas as pd 
import numpy as np

read_data=pd.read_excel("C:/Users/SAGAR GUPTA/Downloads/Mainfile.xlsx")
df=pd.DataFrame(read_data)

# print(df)
# print(df.columns)
########################  1  st Table ####################################
# df1=df.drop(columns=['Sales_person', 'Team', 'Picture',
#        'Product', 'Category', 'Cost_per_box', 'Geo', 'Region'])

# df1.to_csv("C:/Users/SAGAR GUPTA/Downloads/chocolatedata.csv",index=False)
# print(df1.columns)

####################2 nd Table ####################################################

# group_data=df.groupby(['Product','Category','PID'])['Cost_per_box'].mean().reset_index()
# df2=group_data.sort_values(by=['PID'],ascending=True)
# print(df2)
# df2.to_csv("C:/Users/SAGAR GUPTA/Downloads/Groupchocolate.csv",index=False)

############################# 3rd table###########################################

# location=df[['Geo','Region','GID']]
# duplicate_rem=location.drop_duplicates(subset=['Geo','Region','GID'])
# sort_GID=duplicate_rem.sort_values(by='GID',ascending=True)
# sort_GID.to_csv("C:/Users/SAGAR GUPTA/Downloads/LocationChocolate.csv",index=False)
# print(sort_GID)


################################## 4th table############################################


# sales_data=df[['Sales_person','Team','Picture','SPID']]
# rem_dup=sales_data.drop_duplicates(subset=['Sales_person','Team','Picture','SPID'])
# rem_dup.sort_values(by='SPID',inplace=True)
# rem_dup.to_csv("C:/Users/SAGAR GUPTA/Downloads/Salesperson.csv",index=False)
# print(rem_dup)


# location wise total amount
#product wise sales and costing  ,prodict sales req, costing req
#top five selling product 
#order shipment ,count of all diliver , shiped all count diffrencicate all

#product wise sales and costing  ,prodict sales req, costing req
df['Costing']=df['Cost_per_box']*df['Boxes']
df4=df.groupby('Product').agg[{'Amount':'sum','Costing':'sum'}]
print(df4)

# location wise total amount
# l_sales=df.groupby(['Geo'])['Amount'].sum().reset_index(name='Total_Sales')
# print(l_sales)
# l_sales.to_csv("C:/Users/SAGAR GUPTA/Downloads/TotalSales.csv",index=False)

#top five selling product 

# top_sales=df.groupby('Product').value_counts()
# top_five=top_sales.sort_values(by='Amount',ascending=False).head(5)
# print(top_sales)

#order shipment ,count of all diliver , shiped all count diffrencicate all
# count1=df['Order_Status'].value_counts().reset_index()
# print(count1)