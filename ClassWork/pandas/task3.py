import pandas as pd
import numpy as np

#carat=0-0.2 "less than 0.2"
#0.2-0.5  "0.2-0.5"
#0.5-1 "0.5-1"
#>1  "" 

dt=pd.read_csv("C:/Users/SAGAR GUPTA/Downloads/diamonds.csv")
df=pd.DataFrame(dt)
df['Carat_Filter']=np.where(df['carat']<0.2,"Less than 0.2",
        np.where((df["carat"]>=0.2) & (df['carat']<0.5),"0.2-0.5",
        np.where((df['carat']>=0.5) & (df['carat']<=1),"0.5-1","More Than 1")))
print(df.head(100))
