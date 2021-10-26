import mysql.connector as mysql
import streamlit as st


def connection():
    conn = mysql.connect(**st.secrets["mysql"])
    return conn

