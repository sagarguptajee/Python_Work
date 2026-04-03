import pandas as pd
import numpy as np

# s1=pd.Series([1,2,55,4,97,6,5])
# print(s1)
# print(type(s1))

# s1=pd.Series([1,3,5,pd.NaT,None,np.nan])
# print(s1)
# s2=pd.Series({2:'a',1:'b',3:'c'})
# s2=pd.Series({2:'a',1:'b',3:'c'},index=[22,5])
# print(s2)

# s3=pd.Series([10,20],index=[120,140])
# print(s3)


# s4=pd.Series(5,index=[100,20,10])
# print(s4)

# DataFrame
# df=pd.DataFrame({'Name':["Ajay","Vijay","Sunil"],'Bz':[4,5,6],'CD':[7,8,9]})

# print(df)

# dt=pd.read_csv("C:/Users/SAGAR GUPTA/Downloads/Superstore .csv",encoding='latin-1')    #UTF8 Error
# dt=pd.read_csv("C:/Users/SAGAR GUPTA/Downloads/diamonds.csv")
# print(dt)

# dt.to_csv("C:/Users/SAGAR GUPTA/Downloads/Newdiamond.csv")

# print(dt.head(8))
# print(dt.tail())
# print(dt.info())
# print(dt.describe())
# print(dt.shape)
# print(dt.columns)
# print(dt.dtypes)

# dt=pd.Series([1,2,3],[4,5,6])
dt=pd.DataFrame([1,2,3],[4,5,6])
print(dt)
print(type(dt))



