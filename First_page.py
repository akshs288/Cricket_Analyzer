import streamlit as st
import pandas as pd
import plotly.express as px

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
        print(e)      
        
    runs_0 = int(list(df_bat_o.loc[df_bat_o["Player"].str.split("(").str[0].str.strip() == name,"0"])[0])
    st.title("Statistics of 4 and 6")

    colx,coly = st.columns(2)
    data = {"category":["4 runs","6 runs","0 runs"],"Runs":[boundaries_4,boundaries_6,runs_0]}
    new_df = pd.DataFrame(data)
    
    fig = px.pie(new_df,values="Runs",names="category")
    with colx:
        pass

    with coly:
        st.plotly_chart(fig,use_container_width=True)
        

def detail_bowl_player(name,file_path_o,file_path_t20,file_path_test):
    df_bowl_o = pd.read_csv(file_path_o)
    df_bowl_t20 = pd.read_csv(file_path_t20)
    df_bowl_test = pd.read_csv(file_path_test)

    odi_name = df_bowl_o["Player"].str.split("(").str[0]
    t20_name = df_bowl_t20["Player"].str.split("(").str[0]
    test_name = df_bowl_test["Player"].str.split("(").str[0]
    
    tot_Wick = 0
    tot_match = 0
    tot_runs = 0
    tot_balls = 0
    
    def avg_eco_bow(name_of_player):
        Avg_ = 0
        eco = 0
        if name_of_player in odi_name.values:
            Avg_ += float(list(df_bowl_o.loc[df_bowl_o["Player"].str.split("(").str[0] == name_of_player,"Ave"])[0])
            eco += float(list(df_bowl_o.loc[df_bowl_o["Player"].str.split("(").str[0] == name_of_player,"Econ"])[0])
            
        elif name_of_player in t20_name.values:
            Avg_ += float(list(df_bowl_t20.loc[df_bowl_t20["Player"].str.split("(").str[0] == name_of_player,"Ave"])[0])
            eco += int(list(df_bowl_t20.loc[df_bowl_t20["Player"].str.split("(").str[0] == name_of_player,"Ave"])[0])
        
        elif name_of_player in test_name.values:
            Avg_ += float(list(df_bowl_test.loc[df_bowl_test["Player"].str.split("(").str[0] == name_of_player,"Ave"])[0])
            eco += float(list(df_bowl_test.loc[df_bowl_test["Player"].str.split("(").str[0] == name_of_player,"Ave"])[0])
        
        return Avg_,eco


    if name in odi_name.values:
        wik_bowler_o = int(list(df_bowl_o.loc[df_bowl_o["Player"].str.split("(").str[0] == name,"Wkts"])[0])
        tot_Wick += wik_bowler_o
        
        mat_o = int(list(df_bowl_o.loc[df_bowl_o["Player"].str.split("(").str[0] == name,"Mat"])[0])
        tot_match += mat_o
        
        runs_o = int(list(df_bowl_o.loc[df_bowl_o["Player"].str.split("(").str[0] == name,"Runs"])[0])
        tot_runs += runs_o
                
        bow_o = int(list(df_bowl_o.loc[df_bowl_o["Player"].str.split("(").str[0] == name,"Balls"])[0])
        tot_balls += bow_o
        
        total_4 = int(list(df_bowl_o.loc[df_bowl_o["Player"].str.split("(").str[0] == name,"Balls"])[0])
        
        
        
    if name in t20_name.values:
        wick_bowler_t20 = int(list(df_bowl_t20.loc[df_bowl_t20["Player"].str.split("(").str[0] == name,"Wkts"])[0])
        tot_Wick += wick_bowler_t20
    
        mat_t20 = int(list(df_bowl_t20.loc[df_bowl_t20["Player"].str.split("(").str[0] == name,"Mat"])[0])
        tot_match += mat_t20
    
        runs_t20 = int(list(df_bowl_t20.loc[df_bowl_t20["Player"].str.split("(").str[0] == name,"Runs"])[0])
        tot_runs += runs_t20
        
        bow_t20 = int(list(df_bowl_t20.loc[df_bowl_t20["Player"].str.split("(").str[0] == name,"Overs"])[0])*6
        tot_balls += bow_t20
        
    
    if name in test_name.values:
        wick_bowler_test = int(list(df_bowl_test.loc[df_bowl_test["Player"].str.split("(").str[0] == name,"Wkts"])[0])
        tot_Wick += wick_bowler_test
        
        mat_test = int(list(df_bowl_test.loc[df_bowl_test["Player"].str.split("(").str[0] == name,"Mat"])[0])
        tot_match += mat_test
        
        runs_test = int(list(df_bowl_test.loc[df_bowl_test["Player"].str.split("(").str[0] == name,"Runs"])[0])
        tot_runs += runs_test
        
        bow_test = int(list(df_bowl_test.loc[df_bowl_test["Player"].str.split("(").str[0] == name,"Balls"])[0])
        tot_balls += bow_test

    col9,col10,col11,col12 = st.columns(4)
    col13,col14,col15,col16 = st.columns(4)
    
    Avg,Economy = avg_eco_bow(name)
    # # Now defining Stats
    col9.metric("Total Wickets🎯",tot_Wick,border = True)
    col10.metric("Total Matches⚡",tot_match,border = True)
    col11.metric("Average🔥",Avg,border = True)
    col12.metric("Economy💣",Economy,border = True)
    col13.metric("Total Balls🥎",tot_balls,border = True)
    col14.metric("Total Runs🏏",tot_runs,border = True)

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
    st.write("Key Bowling Stats📊")
    # file_path_o,file_path_t20,file_path_test
    detail_bowl_player(name2,"D:\\All Coding files\\DATA SETS\\Cricket\\odbo.csv","D:\\All Coding files\\DATA SETS\\Cricket\\twbo.csv","D:\\All Coding files\\DATA SETS\\Cricket\\tbo.csv")
