import pandas as pd
import streamlit as st

df = pd.read_csv("la_liga.csv")


home_games_df = df[df['home_team'].str.contains('FC Barcelona | barcelona', case=False, na=False)]
away_games_df = df[df['away_team'].str.contains('FC barcelona | barcelona', case=False, na=False)]

def select_home_or_away(df, side):
    return df[df[str(side)].str.contains('FC Barcelona | barcelona', case=False, na=False)]

#STREAMLIT APP
st.title('FC Barcelona Dash Board ⚽️ 🇪🇸')
st.subheader('2024/2025 FC Barcelona Interactive Dashboard')
st.divider()


st.subheader('Select Competition')

competition = st.selectbox(' ',['La Liga','Champions League'], placeholder='Competitions',index=None)
#side = st.selectbox('Select side',['Home','Away'], placeholder='Side',index=None)
# def filter_data(df):
#     if competition:
#         df = 
#         st.dataframe(df)
#st.dataframe(side,hide_index=True)