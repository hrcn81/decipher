import streamlit as st

st.title('Title -> GeeksForGeeks')              # Title
st.header('Header -> GeeksForGeeks')            # Header
st.subheader('Subheader -> GeeksForGeeks')      # SubHeader
st.text('Text -> GeeksForGeeks')                # Text

# st.markdown('# Hi_1')                           # Markdowns
# st.markdown('## Hi_2')
# st.markdown('### Hi_3')
# st.markdown('#### Hi_4')
# st.markdown('##### Hi_5')
# st.markdown('###### Hi_6')
# st.markdown('Hi')

st.success('Success!')                # Success
st.info('Information!')               # Info
st.warning('Warning!')                # Warning 
st.error('Error!')                    # Error

st.exception(ZeroDivisionError('Division not possible'))

st.help(ZeroDivisionError)             # Help

st.write('range(1,10)')                # O|P : range(1,10)
st.write(range(1,10))                  # O|P : range(1,10)
st.write('1+2+3')                      # O|P : 1+2+3
st.write(1+2+3)                        # O|P : 6

st.code('x = 10\n'                      # Code
        'for i in range(x):\n'
            '   print(i)')

st.checkbox('Check')                    # Checkbox
if(st.checkbox('Teen or Kid')):
    st.write('you can\'t proceed further')
# st.checkbox('Male')                   # Can't create same checkbox
if(st.checkbox('Adult')):
    st.write('You are an adult!.....Proceed further')

st.subheader('Radio button')            # Radio Button   
rb = st.radio('Select Gender: ',('Male','Female','Other'))
if(rb == 'Male'):
    st.write("You're a Male")
elif(rb == 'Female'):
    st.write("You're a Female")
elif(rb == 'Others'):
    st.write("you're from Others")

st.subheader('Select Box')              # Select Box
sb = st.selectbox("Data Science : ",[   'Data Analysis','Web Scrapping',
                                        'Machine Learning','NLP',
                                        'Computer Visison','Image Processing'])
st.write("You've selected : ",sb)

st.subheader('Multi Select box')         # Multi select box
msb = st.multiselect("Data Science : ",[   'Data Analysis','Web Scrapping',
                                        'Machine Learning','NLP',
                                        'Computer Visison','Image Processing'])
st.write("You've selcted : ",len(msb),'courses')

st.subheader('Button')                   # Button
# st.button('Click me!')
if(st.button('Click me!')):
    st.write('Thanks for clicking me')

st.subheader('Slider')                   # Slider
vl= st.slider('Select the volume level:',1.0,100.0,step = 0.25)
st.write("your Volume is: ",vl)
# For float steps you've to keep all values as float
ag = st.slider('Select your Age:',18,80,step = 1)
st.write("Your age is: ",ag)

st.subheader('User Input')               # Text_input
username = st.text_input('Username:')
password = st.text_input('Password:',type = 'password')

st.subheader('Text Area')
st.text_area("write something about  your self in 20 words",height = 20)

st.subheader('Input Number')
st.number_input('Input Number',18,100)

st.subheader('Input Date')
st.date_input('Date :')

st.subheader('Input Time')
st.time_input('Time :')















