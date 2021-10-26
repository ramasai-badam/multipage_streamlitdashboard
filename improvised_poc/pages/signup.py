import streamlit as st
from pages import connection,  password_encryptor
import re


def app():
    conn = connection.connection()

    signup_form = st.form(key='sform')
    email = signup_form.text_input(label='EMAIL')
    username = signup_form.text_input(label='USERNAME')
    pwd = signup_form.text_input(label='PASSWORD' , type='password')
    submit_button = signup_form.form_submit_button('SIGNUP')

    if email and username and pwd != '' and submit_button :
        cur = conn.cursor()
        cur.execute('SELECT * FROM users WHERE mail = %s ', (email,))
        account = cur.fetchone()
        if account:
            st.warning('Account already exists')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            st.warning('Invalid email address!')
        else:
           pwd = password_encryptor.create_bcrypt_hash(pwd)
           cur.execute('INSERT INTO USERS VALUES (%s,%s,%s)',(username,email,pwd))
           conn.commit()
           st.success('Account created successfully')
           st.balloons()
        
    conn.close()