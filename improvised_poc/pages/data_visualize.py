import streamlit as st

def app():
    if 'Loggedin' not in st.session_state :
        st.warning('Please log in MF Jones')
    else :
        filter_expander = st.expander('Filter' , expanded=False)
        with filter_expander:
            chk1,chk2,chk3,chk4 = st.columns(4)
            val1 = chk1.checkbox('Alarm type')
            val2 = chk2.checkbox('Severity')
            val3 = chk3.checkbox('Cause')
            val4 = chk4.checkbox('Date')
            print(chk1,chk2,chk3,chk4)
            with st.form(key='columns_in_form'):
                col1,col2,col3,col4 = st.columns([1,1,1,2])
                if val1 : 
                    col1.selectbox('ALARM TYPE',[1,2,3,4])
                if val2 : 
                    col2.selectbox('SEVERITY',[1,2,3,4])
                if val3 : 
                    col3.selectbox('CAUSE',[1,2,3,4])
                if val4 : 
                    col4.date_input('DATE')    
                
                submitted = st.form_submit_button('submit')
   
