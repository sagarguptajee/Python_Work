import pandas as pd
import numpy as np

df0=pd.DataFrame({'Roll_no':[1,2,3,4,5],'Name':['Ajay','Vijay','sinil','Akshay','Krunal'],'marks':[30,21,30,63,14]})

print(df0)

df1=df0.rename(columns={'Roll_no':'RN','marks':'Marks'})
print(df1)

# df2=df1.sort_values(by='Marks',ascending=False)
# print(df2)

df2=df1.sort_values(by=['Marks','Name'],ascending=[True,True])

print(df2)

df3=df2.set_index('RN')

print(df3)