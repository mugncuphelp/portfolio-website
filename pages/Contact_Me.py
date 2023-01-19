import streamlit as st
from send_email import send_email

st.header('Contact Me')

with st.form(key='user_send_email_form'):
    user_email = st.text_input('Enter your email address', key='user_email')
    raw_message = st.text_area('Enter your message', key='message')
    message = f"""\
Subject: Message from Portfolio Website from {user_email}

From: {user_email}
{raw_message}

"""
    submit_button = st.form_submit_button()
    if submit_button:
        send_email(message)
        st.info("Your email was sent succesfully")
