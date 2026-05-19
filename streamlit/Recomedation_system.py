import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors



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


# st.write(ratings_df)
# df1=pd.pivot_table(ratings_df,values='Rating',index='Movie_id',columns='user_id',aggfunc='mean',fill_value=0)
# st.write(df1)

item_base = st.sidebar.checkbox("Item base")
if item_base:
    merge_df = pd.merge(ratings_df,movies_df,on="Movie_id",how="left")
    df1 = pd.pivot_table(merge_df,values='Rating',index='Movie_name',columns='user_id',aggfunc='mean',fill_value=0)

    con_matrix = cosine_similarity(df1)
    df2 = pd.DataFrame(con_matrix,index=df1.index,columns=df1.index)


    sel1 = st.selectbox("Select Movie",movies_df['Movie_name'])
    sel2 = st.button("Fetch Results")
    if sel2:
        rec1 = df2[[sel1]].sort_values(by=sel1,ascending=False).reset_index()
        rec2 = rec1[rec1['Movie_name']!=sel1]
        st.write(rec2.head())

user_base = st.sidebar.checkbox("User Base")
if user_base:
    merge_df = pd.merge(ratings_df, movies_df, on="Movie_id", how="left")
    df1 = pd.pivot_table(merge_df, values='Rating', index='user_id', columns='Movie_name', aggfunc='mean', fill_value=0)
    #st.dataframe(df1)

    model_knn = NearestNeighbors(metric='cosine', algorithm='brute')
    model_knn.fit(df1)

    sel3 = st.number_input("Enter your User ID",1,6040,5,1)
    sel4 = st.button("Fetch Results")
    if sel4:
        distances, indices = model_knn.kneighbors([df1.loc[sel3]], n_neighbors=4)
        user_id_rec = []
        for i in indices:
            df2 = df1.reset_index()
            user_id_rec.append(df2.iloc[i]['user_id'])
            #st.write(df2.iloc[i].get("user_id"))

        user_watched = merge_df[merge_df['user_id']==sel3]
        Rec_list1 = merge_df[merge_df['user_id'].isin(user_id_rec[0])]

        Rec_list = Rec_list1[~Rec_list1['Movie_name'].isin(user_watched['Movie_name'])]
        st.write(Rec_list['Movie_name'].head())

