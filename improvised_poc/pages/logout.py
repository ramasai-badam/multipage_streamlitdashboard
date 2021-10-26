import streamlit as st

def app():
    if 'Loggedin' in st.session_state :
        del st.session_state.Loggedin
        st.error('Logged out')