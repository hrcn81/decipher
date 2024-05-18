import streamlit as st
from datetime import datetime

st.subheader('Text Input')
name = st.text_input('Enter your Name : ')
st.write('Hello !',name)

st.subheader('Password')
password = st.text_input('Enter password :',type = 'password',max_chars = 10,help = "Atleast've 8 characters")

st.subheader('Text Area')
st.text_area('Tell me about your self:',height = 200,max_chars = 500,help = 'Maximum 500 characters')

st.subheader('Numeric input')
st.number_input('Enter your Age : ',min_value = 0,max_value = 110,step = 1,value = 25)

today = datetime.now().date()

date = st.date_input('Enter Date : ',value = today,min_value = datetime.min.date())