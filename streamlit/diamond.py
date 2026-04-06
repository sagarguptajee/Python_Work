import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")
@st.cache_data
def get_data():
    df=pd.read_csv("C:/Users/SAGAR GUPTA/Downloads/diamonds.csv")
    df1=df.drop(columns=['Unnamed: 0'])
    return df1
data_frame=get_data()

b1=st.sidebar.radio("Select your Option",['Overview','EDA Report','Model Training','Prediction'])

if b1=="Overview":
    st.title("Diamond Overview")
    st.write("---")

    st.markdown("<h1>Data Set</h1>",unsafe_allow_html=True)
    st.dataframe(data_frame)
# st.write(b1)

#----------------------EDA------------------------------------
if b1=="EDA Report":
    eda1=st.selectbox("Select Type",['Descriptive Statistic','Univariate Analysis','Bivariate Analysis','Multivariate Analysis'])
    if eda1=="Descriptive Statistic":
        st.markdown("<h2>Describe</h2>",unsafe_allow_html=True)
        st.write(data_frame.describe())

    if eda1=="Univariate Analysis":
        select_col=st.selectbox("Select Column",data_frame.columns)    

        if data_frame[select_col].dtype=="object":
            count_table=data_frame[select_col].value_counts().reset_index()
            st.dataframe(count_table)

            fig1=px.bar(count_table,x=select_col,y='count')
            st.plotly_chart(fig1)

            fig2=px.pie(count_table,values='count',names=select_col)
            st.plotly_chart(fig2)
        else:

            fig1=px.histogram(data_frame[select_col])
            st.plotly_chart(fig1)

            fig2=px.box(data_frame[select_col])
            st.plotly_chart(fig2)