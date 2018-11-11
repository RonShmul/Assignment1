# problems in q1: error in the beginning, not read the table from 2020, how to present the table
# TODO: rearrange the code in functions

import pandas as pd
from bs4 import BeautifulSoup
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
wiki = "https://en.wikipedia.org/wiki/Gal_Gadot"
page = urlopen(wiki)
soup = BeautifulSoup(page)

# print the page
# print(soup.prettify())

# find the films table
films_table = soup.find('table', class_='wikitable sortable')
col1 = []
col2 = []
col3 = []
col4 = []
year = ""
title = ""
role = ""
director = ""
# take every row in the table and insert to cols
for row in films_table.findAll("tr"):
    cells = row.findAll('td')
    heads = row.findAll('th')
    if len(cells) == 5:  # Only extract table body not heading
        col1.append(cells[0].find(text=True))
        year = cells[0].find(text=True)
        col2.append(cells[1].find(text=True))
        title = cells[1].find(text=True)
        col3.append(cells[2].find(text=True))
        role = cells[2].find(text=True)
        col4.append(cells[3].find(text=True))
        director = cells[3].find(text=True)
    if len(cells) == 4:
        temp_year = cells[0].find(text=True)
        if temp_year.isdigit():
            col1.append(cells[0].find(text=True))
            col2.append(cells[1].find(text=True))
            col3.append(role)
            col4.append(cells[2].find(text=True))
        else:
            col1.append(year)
            col2.append(cells[0].find(text=True))
            col3.append(cells[1].find(text=True))
            col4.append(cells[2].find(text=True))
    if len(cells) == 3:
        col1.append(year)
        col2.append(cells[0].find(text=True))
        col3.append(role)
        col4.append(cells[1].find(text=True))

# import pandas to convert list to data frame
df = pd.DataFrame(col1, columns=['Year'])
df['Title'] = col2
df['Role'] = col3
df['Director'] = col4
df
