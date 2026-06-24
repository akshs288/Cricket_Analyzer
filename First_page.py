import streamlit as st
import pandas as pd


st.title("Cricket Dashboard")



cola,colb = st.columns(2)
with cola:
    if st.button("Batsman"):
        name = st.selectbox("Batting",["Aksh","Sameer","Dawood"])
        st.write("You have selected",name)
    
