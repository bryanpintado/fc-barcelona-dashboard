import pandas as pd
import streamlit as st

df = pd.read_csv("la_liga.csv")


home_games_df = df[df['home_team'].str.contains('FC Barcelona | barcelona', case= False, na=False)].reset_index(drop=False)
away_games_df = df[df['away_team'].str.contains('FC barcelona | barcelona',case=False,na=False)]


#STREAMLIT APP
st.title('FC Barcelona Dash Board')
st.divider()


st.header('Home Games')
st.dataframe(home_games_df)  