import pandas as pd
import numpy as np

# index1=[('California',2010),('California',2020),('New Yourk',2010),('New Yourk',2020),('Texas',2010),('Texas',2020)]

# population=[37259645,7594795,47584688,178119856,184754841,4876518945]

# pop=pd.Series(population, name='population',index=index1)

# print(pop)

# index1=[('A',1),('A',2),('A',3),
#         ('B',1),('B',2),('B',3)]
# marks=[20,30,40,50,60,70]

# sr=pd.Series(marks, name='population',index=index1)

# print()


array1=[['A','A','A','B','B','B'],[1,2,3,1,2,3]]
tupple1=[('A',1),('A',2),('B',1),('B',2),('B',3),('B',4),]
produsct1=[['A','B','C'],[1,2]]


index1=pd.MultiIndex.from_arrays(array1,names=('Class','Roll No'))

df=pd.DataFrame({"Marks":[10,20,30,40,50,60]}, index=index1)
print(df)

# df.to_csv("C:/Users/SAGAR GUPTA/Downloads/Student.csv")

# df=df.droplevel("Roll No")
print(df)
df1=df
# df1=df.reset_index()
# print(df1)

df1 = df1.transpose()
print(df1)





