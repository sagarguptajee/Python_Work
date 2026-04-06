import pandas as pd
import numpy as np

df=pd.read_csv("C:/Users/SAGAR GUPTA/Downloads/diamonds.csv")

# df['New']=np.where(df['cut']=='Ideal','Yes','No')
# df['New_Price']=np.where(df['cut']=='Ideal',df['price']*2,df['price'])
# df['New_Price']=np.where((df['cut']=='Ideal')|(df['cut']=='Premium'),df['price']*2,df['price'])
# df['New1']=np.where(df['color'].isin(['D','E','F']),'Yes','No')
# print(df.head(10))

df['Depth_Group']=np.where(df['depth']<=60,"Less than 60" ,
                             np.where(df['depth']<65,"60-65",
                                      np.where(df['depth']<70,"60-70","more than 70") )  )

print(df.head(10))

#carat=0-0.2 "less than 0.2"
#0.2-0.5  "0.2-0.5"
#0.5-1 "0.5-1"
#>1  "" 

#pd.piot()
#pd.piot_table()
#pd.crosstab()
#pd.melt()
#unstack()




# location wise total amount
#product wise sales and costing  ,prodict sales req, costing req
#top five selling product 
#order shipment ,count of all diliver , shiped all count diffrencicate all