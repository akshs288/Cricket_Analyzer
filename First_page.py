import streamlit as st
import pandas as pd

st.title("Cricket Dashboard🏏")

if "bat_or_bal" not in st.session_state:
    st.session_state["bat_or_bal"] = None

cola,colb = st.columns(2)
with cola:
    if st.button("Batsman"):
        st.session_state["bat_or_bal"] = "Batsman"
        
with colb:
    if st.button("Bowler"):
        st.session_state["bat_or_bal"] = "Bowler"

def detail_bat_player(name,file_path):
    df_bat = pd.read_csv(file_path)
    Span_years = list(df_bat.loc[df["Player"].str.split("(").str[0] == name,"Span"])[0]
    odi_runs = list(df_bat.loc[df["Player"].str.split("(").str[0] == name,"Runs"])[0]
    average = list(df_bat.loc[df["Player"].str.split("(").str[0] == name,"Ave"])[0]
    highest_Run = list(df_bat.loc[df["Player"].str.split("(").str[0] == name,"HS"])[0]
    strike_r = list(df_bat.loc[df["Player"].str.split("(").str[0] == name,"SR"])[0]
    boundaries_4 = list(df_bat.loc[df["Player"].str.split("(").str[0] == name,"4s"])[0]
    boundaries_6 = list(df_bat.loc[df["Player"].str.split("(").str[0] == name,"6s"])[0]
    century = list(df_bat.loc[df["Player"].str.split("(").str[0] == name,"100"])[0]
    half_c = list(df_bat.loc[df["Player"].str.split("(").str[0] == name,"50"])[0]
    innings = list(df_bat.loc[df["Player"].str.split("(").str[0] == name,"Inns"])[0]
    col1,col2,col3,col4 = st.columns(4)
    col5,col6,col7,col8 = st.columns(4)
    
    # Now defining Stats
    col1.metric("ODI Runs",odi_runs,border = True)
    col2.metric("ODI Average",average,border = True)
    col3.metric("Highest Run",highest_Run,border = True)
    col4.metric("Total Century",century,border = True)
    col5.metric("Total Half-Century",half_c,border = True)
    col6.metric("Total innings",innings,border = True)

if st.session_state["bat_or_bal"] == "Batsman":
    df = pd.read_csv("D:\All Coding files\DATA SETS\Cricket\odb.csv")
    df2 = df["Player"].str.split("(").str[0]
    dat = sorted(list(df2))
    name = st.selectbox("Batting",dat)
    st.write("Batting Stats📊")
    st.write("For ODI(One Day International)")
    detail_bat_player(name,"D:\All Coding files\DATA SETS\Cricket\odb.csv")


elif st.session_state["bat_or_bal"] == "Bowler":
    df_bow = pd.read_csv("D:\All Coding files\DATA SETS\Cricket\odbo.csv")
    df4 = df_bow["Player"].str.split("(").str[0]
    dat2 = sorted(list(df4))
    name2 = st.selectbox("Bowling",dat2)
    st.write("Key Bowling Stats")
    matches = list(df_bow.loc[df_bow["Player"].str.split("(").str[0] == name2,"Mat"])
    wickets = list(df_bow.loc[df_bow["Player"].str.split("(").str[0] == name2,"Wkts"])
    Avg = list(df_bow.loc[df_bow["Player"].str.split("(").str[0] == name2,"Avg"])
    Economoy = list(df_bow.loc[df_bow["Player"].str.split("(").str[0] == name2,"Econ"])
    tot_ball = list(df_bow.loc[df_bow["Player"].str.split("(").str[0] == name2,"Balls"])
    
    
    