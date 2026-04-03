import pandas as pd
import numpy as np

# df1=pd.DataFrame({"name":['alferd','batman','catwoman'],
#                   "toy":[np.nan,'batmobile','bullship'],
#                   "born":[pd.NaT,pd.Timestamp("1940-04-25"),None]})
# print(df1)

# df2=df1.dropna()
# print(df2)


df3=pd.DataFrame([[np.nan,2,np.nan,0],
                  [3,4,np.nan,1],
                  [np.nan,np.nan,np.nan,np.nan],
                  [np.nan,3,np.nan,4]],
                  columns=["A","B","C","D"])
print(df3)


df=df3.fillna(df3.mean())

df3['A'].fillna(df3['A'].mean(),inplace=True) #for specific null column fill value
df3['C'].fillna("-",inplace=True)  #for specific null column fill value
print(df3)