import numpy as np
import pandas as pd

data_url = 'https://github.com/ine-rmotr-projects/project-files/files/4086772/playstore.xlsx'

playstore_df = pd.read_excel(data_url,
                             usecols=['App', 'Rating', 'Installs', 'Genres', 'Rating', 'Last_Updated'],
                             parse_dates=['Last_Updated'])
playstore_df = playstore_df.sort_values(by='Rating', ascending=False).head(25)

print(playstore_df)
