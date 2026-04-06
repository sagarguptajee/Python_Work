import pandas as pd
import numpy as np


# df1=pd.DataFrame({
#                 'ID':[1,2,3],
#                 'Name':['Alice','Bob','Charlie']

# })
# print(df1)
# df2=pd.DataFrame({
#                 'ID':[2,3,4],
#                 'Score':[85,90,88]

# })

# print(df2)

# merged=pd.merge(df1,df2,on='ID',how='left')#how=left,right,inner(both comon id match) ,outer(all data)
# print(merged)

df1=pd.DataFrame({
    'Name':['Alice','Bob','Charlie']},index=[1,2,3])
df2=pd.DataFrame({'Score':[85,90,88]},index=[2,3,4])
print(df1)
print(df2)
joined=df1.join(df2,how='right')
print(joined)