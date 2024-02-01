import numpy as np
import pandas as pd
import sqlite3

# create a new connection to a db in memory
conn = sqlite3.connect(':memory:')

# create a cursor
c = conn.cursor()

# restore the given van_crime_2003.sql dump
c.executescript(open('RDP-Reading-Data-with-Python-and-Pandas-master/unit-1-reading-data-with-python-and-pandas/lesson-12-vancouver-crime-information/files/van_crime_2003.sql', 'r').read())

# your code goes here
van_crime_df = pd.read_sql('SELECT * FROM van_crimes WHERE Hour > 14',  conn)
late_crimes = van_crime_df.loc[van_crime_df['HOUR'] > 18]
dangerous_month_crimes = van_crime_df.loc[:, 'MONTH'].value_counts().head(1)
print(dangerous_month_crimes)