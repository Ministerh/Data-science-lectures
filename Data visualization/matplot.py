# #from matplotlib import pyplot as plt 
# from bs4 import BeautifulSoup as bs
# import requests
# import pandas as pd
# import lxml

# # response = requests.get('https://statisticstimes.com/economy/asian-countries-by-gdp.php')


# with open('Data visualization\stat_site.html', 'r') as file:
#      contents = file.read()


# soup = bs(contents, 'lxml')

# all_table = soup.find_all(name= 'table' )[1]

# # for table in all_table:
# #       print(table.get('tr'))

# # table = soup.find(name= 'table', id= 'table_id')
# # all_td = all_table.find(name='tbody').find_all('td')
# # for element in all_td:
# #      print(element.text)
# df = pd.read_html(str(all_table), skiprows=1, index_col=0)[0]
# df2020 =df['2020'].to_dict()

 
from matplotlib import pyplot as plt 
# list_year = [i for i in range(1950, 2031, 3)]
year = [ 1984, 1986, 1988, 1990, 1992, 1994, 1996, 1998, 2000, 2002, 2004, 2006, 2008, 
        2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024, 2026, 2028, 2030]
population_in_china = [0.55, 0.61, 0.65, 0.72, 0.82, 0.99, 1.07, 1.172, 1.239, 1.283, 1.321, 1.359,
                      1.397, 1.403, 1.409, 1.415, 1.42, 1.428, 1.434, 1.436, 1.441, 1.441, 1.441, 1.441]

population_in_india = [0.497, 0.553, 0.621, 0.781, 0.87, 0.96, 1.053, 1.144, 1.23,
                       1.309, 1.324, 1.339, 1.354, 1.368, 1.397, 1.411, 1.425, 1.438, 1.451, 1.464,
                       1.477, 1.489, 1.501, 1.512]
# now plot using the plt module

#print(plt.style.available)
#to style the plot
plt.style.use('ggplot')
# to make the plot look hand drawn
#plt.xkcd()
# plt.plot(year, population_in_china, label='china')
# plt.plot(year, population_in_india, label= 'India')

# Add marker,linestyle,color
plt.plot(year, population_in_china, 'b--', label='china')
plt.plot(year, population_in_india, 'o-r', label= 'India')

plt.legend()
plt.show()

# using the subplot

# plt.subplot(1,2,1)
# plt.plot(year, population_in_china, label='china', color='r')
# plt.title('Subplot1')
# plt.xlabel('Year')
# plt.ylabel('Population in Billions')
# plt.legend()
# plt.grid(True)

# plt.subplot(1,2,2)
# plt.plot(year, population_in_india, label='india', color='blue')
# plt.title('Subplot2')
# plt.xlabel('Year')
# plt.ylabel('Population in Billions')
# # to display label
# plt.legend()
# plt.tight_layout()
# plt.grid(True)
# plt.show()














