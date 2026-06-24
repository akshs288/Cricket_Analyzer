import streamlit as st
import pandas as pd

st.title("Cricket Dashboard")

if "bat_or_bal" not in st.session_state:
    st.session_state["bat_or_bal"] = None

cola,colb = st.columns(2)
with cola:
    if st.button("Batsman"):
        st.session_state["bat_or_bal"] = "Batsman"
        
with colb:
    if st.button("Bowler"):
        st.session_state["bat_or_bal"] = "Bowler"

if st.session_state["bat_or_bal"] == "Batsman":
    df = pd.read_csv("D:\All Coding files\DATA SETS\Cricket\odb.csv")
    df2 = df["Player"].str.split("(").str[0]
    dat = sorted(list(df2))
    name = st.selectbox("Batting",dat)

elif st.session_state["bat_or_bal"] == "Bowler":
    s = pd.read_csv("D:\All Coding files\DATA SETS\Cricket\odbo.csv")
    df4 = s["Player"].str.split("(").str[0]
    dat2 = sorted(list(df4))
    name2 = st.selectbox("Bowling",dat2)

