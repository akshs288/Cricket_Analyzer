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
    Span_years = list(df_bat.loc[df_bat["Player"].str.split("(").str[0] == name,"Span"])[0]
    odi_runs = list(df_bat.loc[df_bat["Player"].str.split("(").str[0] == name,"Runs"])[0]
    average = list(df_bat.loc[df_bat["Player"].str.split("(").str[0] == name,"Ave"])[0]
    highest_Run = list(df_bat.loc[df_bat["Player"].str.split("(").str[0] == name,"HS"])[0]
    # strike_r = list(df_bat.loc[df["Player"].str.split("(").str[0] == name,"SR"])[0]
    try:
        boundaries_4 = list(df_bat.loc[df_bat["Player"].str.split("(").str[0] == name,"4s"])[0]
        boundaries_6 = list(df_bat.loc[df_bat["Player"].str.split("(").str[0] == name,"6s"])[0]
    except Exception as e:
        pass
    
    century = list(df_bat.loc[df_bat["Player"].str.split("(").str[0] == name,"100"])[0]
    half_c = list(df_bat.loc[df_bat["Player"].str.split("(").str[0] == name,"50"])[0]
    innings = list(df_bat.loc[df_bat["Player"].str.split("(").str[0] == name,"Inns"])[0]
    col1,col2,col3,col4 = st.columns(4)
    col5,col6,col7,col8 = st.columns(4)
    
    # Now defining Stats
    col1.metric("ODI Runs 🎯",odi_runs,border = True)
    col2.metric("ODI Average 💥",average,border = True)
    col3.metric("Highest Run 👑",highest_Run,border = True)
    col4.metric("Total Century 🚀",century,border = True)
    col5.metric("Total Half-Century 🏏",half_c,border = True)
    col6.metric("Total innings 🧱",innings,border = True)
    try:
        col7.metric("Total 4s 4️⃣",boundaries_4,border = True)
        col8.metric("Total 6s 6️⃣",boundaries_6,border = True)
    except Exception as e:
        pass        

def detail_bowl_player(name,file_path):
    matches = list(df_bow.loc[df_bow["Player"].str.split("(").str[0] == name2,"Mat"])[0]
    wickets = list(df_bow.loc[df_bow["Player"].str.split("(").str[0] == name2,"Wkts"])[0]
    Avg = list(df_bow.loc[df_bow["Player"].str.split("(").str[0] == name2,"Ave"])[0]
    Economoy = list(df_bow.loc[df_bow["Player"].str.split("(").str[0] == name2,"Econ"])[0]
    tot_ball = list(df_bow.loc[df_bow["Player"].str.split("(").str[0] == name2,"Balls"])[0]
    run = list(df_bow.loc[df_bow["Player"].str.split("(").str[0] == name2,"Runs"])[0]
        
    col9,col10,col11,col12 = st.columns(4)
    col13,col14,col15,col16 = st.columns(4)
        
    # Now defining Stats
    col9.metric("Total Wickets🎯",wickets,border = True)
    col10.metric("Total Matches⚡",matches,border = True)
    col11.metric("Average🔥",Avg,border = True)
    col12.metric("Economy💣",Economoy,border = True)
    col13.metric("Total Balls🥎",tot_ball,border = True)
    col14.metric("Total Runs🏏",run,border = True)
    

if st.session_state["bat_or_bal"] == "Batsman":
    df = pd.read_csv("D:\\All Coding files\\DATA SETS\\Cricket\\odb.csv")
    df2 = df["Player"].str.split("(").str[0]
    dat = sorted(list(df2))
    name = st.selectbox("Batting",dat)
    st.write("Batting Stats📊")
    st.write("For ODI (One Day International) ⚖️")
    detail_bat_player(name,"D:\\All Coding files\\DATA SETS\\Cricket\\odb.csv")
    st.write("For T20I ⚡")
    st.write("────────────────────────────────────────────────────────────")
    detail_bat_player(name,"D:\\All Coding files\\DATA SETS\\Cricket\\twb.csv")
    st.write("For Test 🧱")
    st.write("────────────────────────────────────────────────────────────")
    detail_bat_player(name,"D:\\All Coding files\\DATA SETS\\Cricket\\tb.csv")


elif st.session_state["bat_or_bal"] == "Bowler":
    df_bow = pd.read_csv("D:\\All Coding files\\DATA SETS\\Cricket\\odbo.csv")
    df4 = df_bow["Player"].str.split("(").str[0]
    dat2 = sorted(list(df4))
    name2 = st.selectbox("Bowling",dat2)
    st.write("Key Bowling Stats")
    st.write("For ODI (One Day International) ⚖️")
    detail_bowl_player(name2,"D:\\All Coding files\\DATA SETS\\Cricket\\odbo.csv")
    st.write("────────────────────────────────────────────────────────────")
    st.write("For T20I ⚡")
    detail_bowl_player(name2,"D:\\All Coding files\\DATA SETS\\Cricket\\twbo.csv")
    st.write("────────────────────────────────────────────────────────────")
    st.write("For Test 🧱")
    detail_bowl_player(name2,"D:\\All Coding files\\DATA SETS\\Cricket\\tbo.csv")
    
    