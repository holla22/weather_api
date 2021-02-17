import sqlite3
import pandas as pd


conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()


# load the data into a Pandas DataFrame
df = pd.read_csv('test_weather.csv')
# write the data to a sqlite table
df.to_sql('weather', conn, if_exists='append', index = False)