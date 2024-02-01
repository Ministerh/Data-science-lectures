import numpy as np
import pandas as pd
import json
from pandas.io.json import json_normalize
import pprint

with open('RDP-Reading-Data-with-Python-and-Pandas-master/unit-1-reading-data-with-python-and-pandas/lesson-10-artists-nested-biography/files/artists.json') as file:
    artist_dict = json.load(file)

artists = json_normalize(artist_dict)

biography = json_normalize(artist_dict,
                           record_path='bio',
                           meta=['name'])
print(artists)
print(biography)