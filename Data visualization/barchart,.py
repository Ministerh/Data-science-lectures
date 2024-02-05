from matplotlib import pyplot as plt
import numpy as np
plt.style.use('fivethirtyeight')

year = [ 2012, 2014, 2016, 2018, 2020, 2022, 2024, 2026, 2028, 2030]
population_in_china = [1.409, 1.415, 1.42, 1.428, 1.434, 1.436, 1.441, 1.441, 1.441, 1.441]
population_in_india = [1.368, 1.397, 1.411, 1.425, 1.438, 1.451, 1.464,1.489, 1.501, 1.512]

width = 0.25
indices= np.arange(len(year))


plt.bar(indices, population_in_china, color='green',  label='china', width= 0.25)
plt.bar(indices + width, population_in_india, color='blue', label= 'India', width= 0.25)
plt.title('population between china and india')
plt.xlabel('Year')
plt.ylabel('Populations in Billions')

plt.xticks(indices + width/2, year)

plt.legend()
plt.tight_layout()
plt.show()
