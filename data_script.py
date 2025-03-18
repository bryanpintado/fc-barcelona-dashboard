from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv
import psycopg2

# text = requests.get('https://www.laliga.com/en-GB/laliga-easports/results/2024-25/gameweek-1').text
# soup = BeautifulSoup(text,'html.parser')
# match_week_options = soup.select('ul.styled__ItemsList-sc-d9k1bl-2 a')
# game_week_links = ['https://www.laliga.com' + link.get('href')  for link in match_week_options[4:]]

# def get_raw_game_week_df(week_number):
#     game_week = game_week_links[week_number - 1]
#     #html from page
#     data = requests.get(game_week).text   
#     #get table and make df
#     df = pd.read_html(data)[0]
#     return df

# def cleaned_df(week_number):
#     raw_df = get_raw_game_week_df(week_number)
#     df = raw_df.dropna(how='all').dropna(axis=1, how='all')
#     columns_to_drop = [df.columns[0],df.columns[3],df.columns[6]]
#     df = df.drop(columns_to_drop, axis=1)
#     df = df.drop_duplicates(keep = False)
#     # remove row if it contains: 'Horario peninsularWatch Match' 
#     df = df.loc[~df['DATE'].str.contains("Horario peninsularWatch Match", na=False)].reset_index(drop=True)
#     df = df.rename(columns = {'DATE': 'date', 'DATETIME': 'time', 'MATCH': 'match', 'REFEREE' : 'referee'})

#     #error handling for matches that have not been played yet
#     def parse_date(x):
#         try:
#             return datetime.strptime(x.split(' ', 1)[1], '%d.%m.%Y').strftime('%Y-%m-%d')
#         except ValueError:
#             return None
#     df['date'] = df['date'].apply(parse_date)
    
#     #if df does not contain '-' in the match column, None/nan will be inserted
#     df['score']  = df['match'].apply(lambda x: f"{x.split('-')[0][-2]} - {x.split('-')[1][1]}" if '-' in x else None)
#     df['match'] = df['match'].apply(lambda x: f"{x.split('-')[0][:-2:]} - {x.split('-')[1][2::]}" if '-' in x else None)
#     df['home_goals'] = df['score'].apply(lambda x: f"{x.split('-')[0][0:1]}" if x else None)
#     df['away_goals'] = df['score'].apply(lambda x: f"{x.split('-')[1][1:2]}" if x else None)
#     df['home_team'] = df['match'].apply(lambda x: f"{x.split('-')[0][:-1]}" if x else None)
#     df['away_team'] = df['match'].apply(lambda x: f"{x.split('-')[1][1:]}" if x else None)
#     df['match_week'] = week_number
#     df = df.dropna(axis=0)
#     return df if df.empty != True else None

# def get_current_dfs():
#     individual_dfs = []
    
#     for week,link in enumerate(game_week_links):
#         week+=1
#         df = cleaned_df(week)
        
#         if df is not None:
#             individual_dfs.append(df)
#         else:
#             break
            
#     return individual_dfs
# individual_dfs = get_current_dfs()

# main_df = pd.concat(individual_dfs, ignore_index=False)
# main_df.reset_index(drop=True)

'''
Moving data to Supabase
'''
load_dotenv()
db_params = {
    "host" : os.getenv("host"),
    "port" : int(os.getenv("port")),
    "dbname" : os.getenv("database"),
    "user" : os.getenv("user"),
    "password" : os.getenv("password")
}

conn = psycopg2.connect(**db_params) 
cursor = conn.cursor()

cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_table (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT NOW()
        );
    """)
conn.commit()

cursor.close()
conn.close()