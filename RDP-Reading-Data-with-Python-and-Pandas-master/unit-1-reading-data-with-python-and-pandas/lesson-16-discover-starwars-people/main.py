import numpy as np
import pandas as pd
import requests

req = requests.get('https://swapi.co/api/people/?format=json')
starwars_people_df = req.json()
print(starwars_people_df)