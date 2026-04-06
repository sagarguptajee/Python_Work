import pandas as pd
import numpy as np


data={
    'Category':['A','A','A','B','B','B','C','C','C',],
    'Region':['East','West','West','West','West','East','East','West','East'],
    'Sales':[100,150,200,250,300,400,100,200,300],
    'Quantity':[1,2,3,4,5,2,5,2,6]
}

df=pd.DataFrame(data)
print(df)

# df1=df.groupby('Category')['Quantity'].mean()
# print(df1)

# df1=df.groupby('Region')['Sales'].agg(['sum','mean','count','min','max'])

# print(df1)

# df1=df.groupby('Region')

df1=df.groupby('Category').agg({'Sales':'mean','Quantity':'sum'})
print(df1)

#df1=df.groupby(['Category','Region'])['Sales'].mean() #min() ,max()



#load diamod data
#carat>0.5,color = d e f, color wise cut wise total price ,rename COLOUR ,CUT,Total Price,color wise ass and price wise dec