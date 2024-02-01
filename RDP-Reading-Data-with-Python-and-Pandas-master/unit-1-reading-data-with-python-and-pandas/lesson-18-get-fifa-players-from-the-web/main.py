import numpy as np
import pandas as pd
import requests




df= pd.read_html('RDP-Reading-Data-with-Python-and-Pandas-master/unit-1-reading-data-with-python-and-pandas/lesson-18-get-fifa-players-from-the-web/files/fifa_players.html', encoding='utf-8')
fifa_df = df[0]

fifa_df= fifa_df.iloc[:, 2:-1]

most_hits_player = fifa_df.sort_values('Hits', ascending=False).head(1)
print(most_hits_player)