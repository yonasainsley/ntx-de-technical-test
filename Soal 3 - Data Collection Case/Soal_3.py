# -*- coding: utf-8 -*-
"""Soal_3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qGJw-COwnwEHdZFUV3iry0GGdVSm35ms
"""

from bs4 import BeautifulSoup
import requests
from re import search
import pandas as pd
import json
import os

"""I have never practically applied asynchronous programming but I understand it in theory, with that and the time constraint of this task in mind, I decided to make a simple synchronous scrapping app."""

# Make datasets directory
os.makedirs('./datasets', exist_ok=True)

# Init list for skipped pages
skipped = []

# Loop for all the urls
for i in range (1,6):

    # Init lists for storing titles and links
    titles = []
    links = []
    for j in range (1,6):
        web = 'https://www.fortiguard.com/encyclopedia?type=ips&risk='+str(i)+'&page='+str(j)
        try:
            # Purposefully make an error to test out skipped.json
            # if i == 3:
            #     asdasd

            page = requests.get(web)
            soup = BeautifulSoup(page.text, 'html')

            # Scrapping the titles
            article_divs = soup.find_all('div', class_='col-lg')
            for div in article_divs:
                title_tag = div.find('b')
                if title_tag:
                    title = title_tag.text.strip()
                    titles.append(title)

            # Scrapping the links
            link_divs = soup.find("div", {"class": "page-content"})
            link_sections = link_divs.find("section", {"class": "table-body"})
            link_rows = link_sections.find_all("div", {"class": "row"})
            for row in link_rows:
                if row.has_attr("onclick"):
                    link = search(r"'/([^']+)'", row["onclick"])
                    link = 'https://www.fortiguard.com/'+link.group(1)
                    links.append(link)

        # When error is caught, the url is appended to skipped list
        except Exception:
            skipped.append(web)

        # Creation of CSV
        df = pd.DataFrame({'Title': titles, 'Link': links})
        name = './datasets/forti_lists_'+str(i)+'.csv'
        df.to_csv(name, index=False)

# Dump all skipped urls into a json
with open('./datasets/skipped.json', 'w') as json_file:
    json.dump(skipped, json_file)

