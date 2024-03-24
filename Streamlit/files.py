import streamlit as st

st.subheader('Uploading CSV file')

df = st.file_uploader('Upload CSV file : ',type = ['csv','xlsx'])
# if df is not None:
#     st.dataframe(df)
# st.table(df)

# import pandas as pd
# st.subheader('Loading CSV file')
# df = pd.read_csv(r"C:\Users\mayan\OneDrive\Desktop\insurance.csv")
# if df is not None:
#     st.table(df.head())

st.subheader('Dealing with images diractly')
st.image(r"D:\OMEN\cosmic.png")

st.subheader('Uploading Image')
img_1 = st.file_uploader("Upload the Image file : ",type = ['png','jpeg','jpg'])
if img_1 is not None:
    st.image(img_1, caption='Uploaded Image', use_column_width=True)

st.subheader('Uploading and showing multiple images')
img_2 = st.file_uploader("Upload the Image file : ", type=['png', 'jpeg', 'jpg'], accept_multiple_files=True)
if img_2 is not None:
    for i in img_2:
        st.image(i, caption='Uploaded Image', use_column_width=True)

st.subheader('Uploading Video')
vd = st.file_uploader('Upload Video file',type = ['mkv','mp4'])
if vd is not None:
    st.video(vd)

st.subheader('Uploading Multiple Video')
vd1 = st.file_uploader('Upload Video file',type = ['mkv','mp4'],accept_multiple_files=True)
if vd1 is not None:
    for i in vd1:
        st.markdown(f"**File Name:** {i.name}")
        st.video(i)

st.subheader('Uploading Audio')
af = st.file_uploader('Upload and audio file :',type = ['mp3','wav'])
if af is not None:
    st.markdown(f"**File Name:** {af.name}")
    st.audio(af)

st.subheader('Uploading multiple Audios')
af1 = st.file_uploader('Upload and audio file :',type = ['mp3','wav'],accept_multiple_files = True)
if af1 is not None:
    for i in af1:
        st.markdown(f"**File Name:** {i.name}")
        st.audio(i)

