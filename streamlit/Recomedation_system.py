import streamlit as st
import pandas as pd



# st.write("Hello")
st.set_page_config(layout='wide')

@st.cache_data
def get_data():
    movies_df=pd.read_csv("C:/Users/SAGAR GUPTA/Downloads/Movie_review/movies.dat",header=None,sep="::",encoding="latin-1")
    movies_df.rename(columns={0:'Movie_id',1:"Movie_name",2:"Type"},inplace=True)


    users_df=pd.read_csv("C:/Users/SAGAR GUPTA/Downloads/Movie_review/users.dat",header=None,sep="::",encoding="latin-1")
    users_df.rename(columns={0:'users_id',1:"Gender",2:"Age_group",3:"Occupation",4:"Zip_code"},inplace=True)


    ratings_df=pd.read_csv("C:/Users/SAGAR GUPTA/Downloads/Movie_review/ratings.dat",header=None,sep="::",encoding="latin-1")
    ratings_df.rename(columns={0:'user_id',1:"Movie_id",2:"Rating",3:"Timestamp"},inplace=True)
    ratings_df['Timestamp']=pd.to_datetime(ratings_df['Timestamp'],unit='s')

    avg_rating=ratings_df.groupby('Movie_id')['Rating'].agg(['count','mean']).reset_index()
    new_df=pd.merge(movies_df,avg_rating,on='Movie_id',how='outer')
    new_df.rename(columns={'mean':'avg_rating','count':'votes'},inplace=True)
    new_df['avg_rating']=round(new_df['avg_rating'],1)

    return new_df,ratings_df,users_df

movies_df,ratings_df,user_df=get_data()

e1=st.sidebar.checkbox("EDA")
if e1:
    st.write("No of movies",movies_df.shape[0])
    st.write("No of users",user_df.shape[0])



st.markdown("Trending Movies")
st.markdown("----------")
s1=movies_df.sort_values(by='avg_rating',ascending=False)
s1=s1[s1['votes']>100]
st.write(s1.head())


st.write(ratings_df)
df1=pd.pivot_table(ratings_df,values='Rating',index='Movie_id',columns='user_id',aggfunc='mean',fill_value=0)
st.write(df1)