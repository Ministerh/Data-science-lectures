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
van_crime_df = pd.read_sql('''SELECT TYPE, MONTH, DAY, NEIGHBOURHOOD FROM van_crimes
                            WHERE NEIGHBOURHOOD IN ("Stanley park", "west end") ''', conn)

crime_types_count = van_crime_df['TYPE'].value_counts()
print(crime_types_count)
