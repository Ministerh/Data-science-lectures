import numpy as np
import pandas as pd
import sqlite3

# create a new connection to a db in memory
conn = sqlite3.connect(':memory:')

# create a cursor
c = conn.cursor()

# restore the given cryptos.sql dump
c.executescript(open('RDP-Reading-Data-with-Python-and-Pandas-master/unit-1-reading-data-with-python-and-pandas/lesson-14-crypto-currency-database/files/cryptos.sql', 'r').read())

# your code goes here
crypto_df = pd.read_sql('SELECT FROM cryptocoins_cryptocurrency, cryptocoins_exchange WHERE ')