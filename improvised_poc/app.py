import os
import streamlit as st


# Custom imports 
from multipage import MultiPage
from pages import login, logout, signup, data_visualize, prediction # import your pages here

# Create an instance of the app 
app = MultiPage()

col1 , col2 = st.columns([6,1])
col1.title("Get to know Alarms better")
col2.button(label='LOGOUT' , on_click = logout.app)



# Add all your application here
app.add_page("Login", login.app)
app.add_page("SignUp", signup.app)
app.add_page("Analysis", data_visualize.app)
app.add_page("Prediction",prediction.app)
# app.add_page("Y-Parameter Optimization",redundant.app)

# The main app
app.run()