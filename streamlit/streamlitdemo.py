import streamlit as st

st.write("hello")

b1=st.checkbox("Subject")

if b1:
    st.write("How are you:")


b2=st.button("click here")

if b2:
    st.write("I am Fine")


b3=st.selectbox("Select Subject",['math','english'])
st.write(b3)


b4=st.multiselect("Select Multi Sub",['math','sci','eng'])
st.write(b4)

st.slider("Range",0,10,2,1)

st.text_area("Write Here")

st.text_input("hgsdhg")

st.number_input("what is your number")