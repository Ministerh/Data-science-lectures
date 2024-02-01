import numpy as np
import pandas as pd

artist_json = pd.read_json('RDP-Reading-Data-with-Python-and-Pandas-master/unit-1-reading-data-with-python-and-pandas/lesson-9-parse-artists-json-file/files/artists.json')
artist_json.drop(['bio'], axis=1, inplace=True)
artist_json.set_index('name', inplace=True)


print(artist_json)
