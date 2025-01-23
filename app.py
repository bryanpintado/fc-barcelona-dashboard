import pandas as pd
import streamlit as st

df = pd.read_csv("league_info.csv")



st.title('FC Barcelona Stats')
st.write(df)  
