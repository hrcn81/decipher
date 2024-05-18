import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20,3),columns = ['Line_1','Line_2','Line_3'])

st.header('1 Charts with random numbers')
st.subheader('1.1 Line Chart')
st.line_chart(chart_data)

st.subheader('1.2 Area Chart')
st.area_chart(chart_data)

st.subheader('1.3 Bar Chart')
st.bar_chart(chart_data)

import matplotlib.pyplot as plt
import seaborn as sns

st.header('2 Data Visualization with Matplotlib and Seaborn')
st.subheader('2.1 Loading Dataframe')
df = pd.read_csv(r"D:\DataScience\Iant\python\streamlit\iris.csv")
st.dataframe(df)

st.subheader('2.2 Bar graph with  matplotlib')
fig = plt.figure(figsize=(15,8))
df['species'].value_counts().plot(kind= 'bar')
st.pyplot(fig)

st.subheader('2.3 Distribution plot with seaborn')
fig = plt.figure(figsize= (15,8))
sns.distplot(df['sepal_length'])
st.pyplot(fig)

st.header('Multiple Graph')
col1,col2 = st.columns(2)
with col1:
    col1.header = 'KDE = False'
    # col1.write('KDE = False')
    fig1 = plt.figure(figsize=(5,5))
    sns.distplot(df['sepal_length'],kde = False)
    st.pyplot(fig1)
with col2:
    col2.header = 'Hist = False'
    # col2.write('Hist = False')
    fig1 = plt.figure(figsize=(5,5))
    sns.distplot(df['sepal_length'],hist = False)
    st.pyplot(fig1)

