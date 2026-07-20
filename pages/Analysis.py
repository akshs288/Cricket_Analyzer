import streamlit as st
import pandas as pd

df_o = pd.read_csv("D:\\All Coding files\\Mega projects\\Cricket Analysis\\odb2.csv")

st.header("Interesting analysis of Cricket")

play_name = df_o.loc[df_o["Runs"] == df_o["Runs"].max(),"Player"]  # This will return series of name
l = play_name.values    # This will return array of name
run_play = df_o["Runs"].max()


st.markdown(f"""
<div style="
background:#1e1e1e;
padding:20px;
border-radius:15px;
border:1px solid #444;
">

<h4>🏏 Most Runs</h4>

<h1 style="color:#4CAF50;">{run_play}</h1>

<h3>{l[0]} 🇮🇳</h3>

<p>Total ODI Runs</p>

</div>
""", unsafe_allow_html=True)


avg_name = list(df_o.loc[df_o["Ave"] == df_o["Ave"].max(),"Player"].values)[0]
avg_val = df_o["Ave"].max()

st.write("")
st.write("")
st.write("")

st.markdown(f"""
<div style="
background:#1e1e1e;
padding:20px;
border-radius:15px;
border:1px solid #444;
">

<h4>🏏 Highest Average</h4>

<h1 style="color:#4CAF50;">{avg_val} </h1>

<h3>{avg_name}</h3>

<p>Highest Average in ODI</p>

</div>
""", unsafe_allow_html=True)



