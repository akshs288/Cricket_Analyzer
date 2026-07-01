import streamlit as st
import pandas as pd

st.title("Cricket Dashboard🏏")

if "bat_or_bal" not in st.session_state:
    st.session_state["bat_or_bal"] = None

cola,colb = st.columns(2)
with cola:
    if st.button("Batsman 🏏"):
        st.session_state["bat_or_bal"] = "Batsman"

with colb:
    if st.button("Bowler 🌀"):
        st.session_state["bat_or_bal"] = "Bowler"

def detail_bat_player(name,file_path_odi,file_path_t20,file_path_test):
    df_bat_o = pd.read_csv(file_path_odi)
    df_bat_t20 = pd.read_csv(file_path_t20)
    df_bat_test = pd.read_csv(file_path_test)

    odi_name = df_bat_o["Player"].str.split("(").str[0].str.strip()
    t20_names = df_bat_t20["Player"].str.split("(").str[0].str.strip()
    test_names = df_bat_test["Player"].str.split("(").str[0].str.strip()

    def total_objects(column_name):
        tot_runs = 0
        if name in odi_name.values:
            tot_runs += (list(df_bat_o.loc[df_bat_o["Player"].str.split("(").str[0].str.strip() == name,column_name])[0])
        
        if name in t20_names.values:
            tot_runs += (list(df_bat_t20.loc[df_bat_t20["Player"].str.split("(").str[0].str.strip() == name,column_name])[0])
        
        if name in test_names.values:
            tot_runs += (list(df_bat_test.loc[df_bat_test["Player"].str.split("(").str[0].str.strip() == name,column_name])[0])
        return tot_runs
    
    sum_avg = 0
    c = 0   
    if name in odi_name.values:
       sum_avg +=  list(df_bat_o.loc[df_bat_o["Player"].str.split("(").str[0].str.strip() == name,"Ave"])[0]
       c += 1
    
    if name in t20_names.values:
        sum_avg +=  list(df_bat_t20.loc[df_bat_t20["Player"].str.split("(").str[0].str.strip() == name,"Ave"])[0]
        c += 1
    
    if name in test_names.values:
        sum_avg +=  list(df_bat_test.loc[df_bat_test["Player"].str.split("(").str[0].str.strip() == name,"Ave"])[0]
        c += 1
        
    final_avg = round(sum_avg/c,2)
    print("Average of the runs are: ",final_avg)
    
    
    highest_Run = ""
    strike_r = ""
    if name in t20_names.values:
        highest_Run = list(df_bat_t20.loc[df_bat_t20["Player"].str.split("(").str[0].str.strip() == name,"HS"])[0]    
        strike_r = list(df_bat_t20.loc[df_bat_t20["Player"].str.split("(").str[0].str.strip() == name,"SR"])[0]

    elif name in odi_name.values:
        highest_Run = list(df_bat_o.loc[df_bat_o["Player"].str.split("(").str[0].str.strip() == name,"HS"])[0]
        strike_r = list(df_bat_o.loc[df_bat_o["Player"].str.split("(").str[0].str.strip() == name,"SR"])[0]
    
    else:
        highest_Run = list(df_bat_test.loc[df_bat_test["Player"].str.split("(").str[0].str.strip() == name,"HS"])[0]
        strike_r = "N/A"
        
    try:
        odi_4 = int(list(df_bat_o.loc[df_bat_o["Player"].str.split("(").str[0].str.strip() == name,"4s"])[0])
        t20_4 = int(list(df_bat_t20.loc[df_bat_t20["Player"].str.split("(").str[0].str.strip() == name,"4s"])[0])
        boundaries_4 = odi_4+t20_4
        
        odi_6 = int(list(df_bat_o.loc[df_bat_o["Player"].str.split("(").str[0].str.strip() == name,"6s"])[0])
        t20_6 = int(list(df_bat_t20.loc[df_bat_t20["Player"].str.split("(").str[0].str.strip() == name,"6s"])[0])
        boundaries_6 = odi_6+t20_6

    except Exception as e:
        print(e)
    
    century = total_objects("100")
    half_c = total_objects("50")
    tot_Runs = total_objects("Runs")
    
    col1,col2,col3,col4 = st.columns(4)
    col5,col6,col7,col8 = st.columns(4)
    
    # Now defining Stats
    col1.metric("Total Runs 🎯",tot_Runs,border = True)
    col2.metric("Average 💥",final_avg,border = True)
    col3.metric("Highest Run 👑",highest_Run,border = True)
    col4.metric("Total Century 🚀",century,border = True)
    col5.metric("Total Half-Century 🏏",half_c,border = True)
    col6.metric("Strike Rate",strike_r,border = True)
    
    try:
        col7.metric("Total 4s 4️⃣",boundaries_4,border = True)
        col8.metric("Total 6s 6️⃣",boundaries_6,border = True)
        
    except Exception as e:
        pass        

def detail_bowl_player(name,file_path_o,file_path_t20,file_path_test):
    df_bowl_o = pd.read_csv(file_path_o)
    df_bowl_t20 = pd.read_csv(file_path_t20)
    df_bowl_test = pd.read_csv(file_path_test)

    
    matches = list(df_bow.loc[df_bow["Player"].str.split("(").str[0] == name2,"Mat"])[0]
    wickets = list(df_bow.loc[df_bow["Player"].str.split("(").str[0] == name2,"Wkts"])[0]
    Avg = list(df_bow.loc[df_bow["Player"].str.split("(").str[0] == name2,"Ave"])[0]
    Economoy = list(df_bow.loc[df_bow["Player"].str.split("(").str[0] == name2,"Econ"])[0]
    tot_ball = list(df_bow.loc[df_bow["Player"].str.split("(").str[0] == name2,"Balls"])[0]
    run = list(df_bow.loc[df_bow["Player"].str.split("(").str[0] == name2,"Runs"])[0]
        
    col9,col10,col11,col12 = st.columns(4)
    col13,col14,col15,col16 = st.columns(4)
        
    # # Now defining Stats
    col9.metric("Total Wickets🎯",wickets,border = True)
    col10.metric("Total Matches⚡",matches,border = True)
    col11.metric("Average🔥",Avg,border = True)
    col12.metric("Economy💣",Economoy,border = True)
    col13.metric("Total Balls🥎",tot_ball,border = True)
    col14.metric("Total Runs🏏",run,border = True)

if st.session_state["bat_or_bal"] == "Batsman":
    df_o = pd.read_csv("D:\\All Coding files\\DATA SETS\\Cricket\\odb.csv")
    df2 = df_o["Player"].str.split("(").str[0].str.strip().to_list()
    df_t2 = pd.read_csv("D:\\All Coding files\\DATA SETS\\Cricket\\twb.csv")
    df3 = df_t2["Player"].str.split("(").str[0].str.strip().to_list()
    df_te = pd.read_csv("D:\\All Coding files\\DATA SETS\\Cricket\\tb.csv")
    df4 = df_te["Player"].str.split("(").str[0].str.strip().to_list()
    
    df = list(set(df2+df3+df4))
    dat = sorted(df)
    name = st.selectbox("Batting",dat)
    st.write("Batting Stats📊")
    
    detail_bat_player(name,"D:\\All Coding files\\DATA SETS\\Cricket\\odb.csv","D:\\All Coding files\\DATA SETS\\Cricket\\twb.csv","D:\\All Coding files\\DATA SETS\\Cricket\\tb.csv")


elif st.session_state["bat_or_bal"] == "Bowler":
    df_bow = pd.read_csv("D:\\All Coding files\\DATA SETS\\Cricket\\odbo.csv")
    df4 = df_bow["Player"].str.split("(").str[0]
    dat2 = sorted(list(df4))
    name2 = st.selectbox("Bowling",dat2)
    st.write("Key Bowling Stats")
    
    
    
    