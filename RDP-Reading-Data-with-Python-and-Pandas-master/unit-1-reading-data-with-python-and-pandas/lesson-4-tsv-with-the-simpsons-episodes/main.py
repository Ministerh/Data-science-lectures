import numpy as np
import pandas as pd

col_names = ['Title', 'Air date', 'Production code', 'Season', 'Number in season',
             'Number in series', 'US viewers (million)', 'Views', 'IMDB rating']

simpson_episodes = pd.read_csv('RDP-Reading-Data-with-Python-and-Pandas-master/unit-1-reading-data-with-python-and-pandas/lesson-4-tsv-with-the-simpsons-episodes/files/simpsons-episodes.tsv',
                               sep = '\t',
                               encoding= 'UTF-8',
                               names=col_names,
                               index_col='Production code',
                               na_values= ['no_val'],
                               parse_dates=['Air date'],
                               usecols= ['Title','Air date', 'Production code', 'IMDB rating'],
                               skiprows=4
                               )

print(simpson_episodes)        
                          