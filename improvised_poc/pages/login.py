import streamlit as st
import bcrypt
from pages import connection,password_encryptor


def app():

    conn = connection.connection()

    Login_form = st.form(key='lform')
    email = Login_form.text_input(label='EMAIL')
    pwd = Login_form.text_input(label='PASSWORD' , type='password')
    submit_button = Login_form.form_submit_button('LOGIN')

    if submit_button :
        cur = conn.cursor()
        cur.execute('SELECT * FROM users WHERE mail = %s ', (email,))
        account = cur.fetchone()
        if account == None :
            st.warning('Wrong email/password')
        elif password_encryptor.verify_password(pwd , account[2] ):
            st.session_state.Loggedin = True
            st.success('Loggedin as '+ str(account[0]))
        

    conn.close()   
    

    

    