import pandas as pd
import numpy as np

#load diamod data
#carat>0.5,color = d e f, color wise cut wise total price ,rename COLOUR ,CUT,Total Price,color wise ass and price wise dec

dt=pd.read_csv("C:/Users/SAGAR GUPTA/Downloads/diamonds.csv")


df1=dt
color_filter=df1[(df1['color']=='D')|(df1['color']=='E')|(df1['color']=='F')]
car_filter=color_filter[color_filter['carat']>0.5]
group_data=car_filter.groupby(['color','cut',])['price'].sum().reset_index()
print(group_data)


df2= group_data.rename(columns={'color':'COLOUR','cut':'CUT','price':'Total Price'})
sort1=df2.sort_values(by=['Total Price','COLOUR'],ascending=[False,True])
print(sort1)




