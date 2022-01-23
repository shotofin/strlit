import streamlit as st
import pandas as pd

st.write("Ma luati si pe mine acasa?")

with st.form("form1", True):
   
    # Every form must have a submit button.
    submittedD = st.form_submit_button("DA")
    submittedN = st.form_submit_button("NU")
    
    if submittedD:
        st.write("THANK YOU! 😀 ")
        
    if submittedN:
        st.write("😭")
        st.write("atunci canta la pian")

