import streamlit as st
import pandas as pd

df_o = pd.read_csv("D:\\All Coding files\\Mega projects\\Cricket Analysis\\odb2.csv")
df_b_o = pd.read_csv("D:\\All Coding files\\Mega projects\\Cricket Analysis\\odbo2.csv")

st.header("Interesting analysis of Cricket")

play_name = df_o.loc[df_o["Runs"] == df_o["Runs"].max(),"Player"]  # This will return series of name
l = play_name.values    # This will return array of name
run_play = df_o["Runs"].max()

# Highest Run of which player

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

# Highest Average of which player

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

# Highest Person who hit sixes
six_name = list(df_o.loc[df_o["6s"] == df_o["6s"].max(),"Player"])[0]
six_num = df_o["6s"].max()

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

<h4>6️⃣ Highest Sixes </h4>

<h1 style="color:#4CAF50;">{six_num} </h1>

<h3>{six_name}</h3>

<p>Highest Number of sixes in ODI</p>

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

# Maximum Wickets taken
max_wick_name = list(df_b_o.loc[df_b_o["Wkts"] == df_b_o["Wkts"].max(),"Player"])[0]
max_wick = df_b_o["Wkts"].max()

st.markdown(f"""
<div style="
background:#1e1e1e;
padding:20px;
border-radius:15px;
border:1px solid #444;
">

<h4>🥎 Highest Wickets </h4>

<h1 style="color:#4CAF50;">{max_wick} </h1>

<h3>{max_wick_name}</h3>

<p>Highest Number of Wickets taken in ODI</p>

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

# Best economy
eco_name = list(df_b_o.loc[df_b_o["Econ"] == df_b_o["Econ"].min(),"Player"])[0]
eco_num = df_b_o["Econ"].min()

st.markdown(f"""
<div style="
background:#1e1e1e;
padding:20px;
border-radius:15px;
border:1px solid #444;
">
<h4>🎯 Best Economy </h4>
<h1 style="color:#4CAF50;">{eco_num} </h1>
<h3>{eco_name}</h3>
<p>One of the best economy in ODI</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

# Most Centuries
name_cent = list(df_o.loc[df_o["100"] == df_o["100"].max(),"Player"])[0]
cent_numbers = df_o["100"].max()

st.markdown(f"""
<div style="
background:#1e1e1e;
padding:20px;
border-radius:15px;
border:1px solid #444;
">
<h4>💯 Most Centuries </h4>
<h1 style="color:#4CAF50;">{cent_numbers} </h1>
<h3>{name_cent}</h3>

<p> Centuries in ODI</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

df_odi_team = pd.read_csv("D:\\All Coding files\\DATA SETS\\Cricket\\odt.csv")
match_name = list(df_odi_team.loc[df_odi_team["Margin"].str[0] == df_odi_team["Margin"].str[2],"Series/Tournament"])[0]
match_record = list(df_odi_team.loc[df_odi_team["Margin"].str[0] == df_odi_team["Margin"].str[2],"Margin"])[0]
country_name = list(df_odi_team.loc[df_odi_team["Margin"].str[0] == df_odi_team["Margin"].str[2],"Winner"])[0]

st.markdown(f"""
<div style="
background:#1e1e1e;
padding:20px;
border-radius:15px;
border:1px solid #444;
">
<h4>🤝 Draw Tournament </h4>
<h1 style="color:#4CAF50;">{match_record} </h1>
<h3>{match_name}</h3>
<h4>Winner of tournament according to ICC :- <h2>{country_name}  </h2> </h4>
<p>Match which are tie in ODI</p>
</div>
""", unsafe_allow_html=True)


st.write("")
st.write("")
st.write("")

questions = ("Which Batter Played highest number of innings ??", "Who has highest not out score ??","")

st.selectbox("Most Frequent Questions are asked",questions)





