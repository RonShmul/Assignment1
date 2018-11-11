import pandas as pd
from bs4 import BeautifulSoup
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
wiki_gal = "https://en.wikipedia.org/wiki/Gal_Gadot"
wiki = "https://en.wikipedia.org"
page = urlopen(wiki_gal)
soup = BeautifulSoup(page, 'html.parser')

films_table = soup.find('table', class_='wikitable sortable')
col1 = []
col2 = []
col3 = []
col4 = []
title = ""
for row in films_table.findAll("tr"):
    cells = row.findAll('td')
    title_tag = ""
    if len(cells) == 0:
        continue
    if len(cells) == 5:
        title_a = cells[1].find('a')
        title_tag = wiki + title_a.get("href")
    else:
        if cells[0].isdigit():
            title_tag = cells[1].find('a')
            title_tag = wiki + title_a.get("href")
        else:
            title_tag = cells[0].find('a')
            title_tag = wiki + title_a.get("href")
    # open the page of the movie
    film_page = urlopen(title_tag)
    film_soup = BeautifulSoup(film_page)
    if film_soup.find(id="Cast"):
        cast = film_soup.find(id="Cast").parent.find_next('ul')
    if film_soup.find(id="Voice_cast"):
        cast = film_soup.find(id="Voice_cast").parent.find_next('ul')
    players = cast.findAll('li')
    # every link of player in the list of movie cast # Todo: fix it, insert the links of players to a list,
    # Todo check if the cast is in more than 1 ul
    for player in players:
        name_a = player.find('a')
        name_tag = wiki + title_a.get("href")
        name = player.find('a').title   # ? # Todo: check if the name is already exist
        # open the page of the actor
        actor_page = urlopen(name_tag)
        soup = BeautifulSoup(actor_page)
        info_table = soup.find('table', class_='infobox biography vcard')

        #col1.append(name_tag) # check if the name is already exist
