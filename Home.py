import streamlit as st
import pandas
import math


def display_app(app_df, start_index):
    if start_index < len(app_df):
        st.title(app_df['title'][start_index])
        st.image(f'images/{app_df["image"][start_index]}')
        st.info(app_df['description'][start_index])
        st.write(f'[Source Code]({app_df["url"][start_index]})')


st.set_page_config(layout='wide')

col1 , col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title('Izzuddin W Jaafar')
    content = '''
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    
    '''
    st.write(content)

content2 = '''
Below you can find some apps that i have built in python. Feel free to contact me
'''
st.write(content2)

start_index = -1

df = pandas.read_csv('data.csv')
for app_row in range(math.ceil(len(df)/2)):
    
    col_left ,col_mid,  col_right = st.columns([1.5, 0.2, 1.5])
    with col_left:
        start_index = start_index + 1
        display_app(df,start_index)

    with col_right:
        start_index = start_index + 1
        display_app(df,start_index)

    st.text(" ")






