import requests
import pandas as pd
import numpy as np

class GoogleApi():
    """ It helps to make google requests and to get resulting links """

    API_KEY = ''
    # API_KEY = 'AIzaSyAYFhT-s-4Q3z_An4iIGHzLSCLnsR98zhg'
    SEARCH_ENGINE_ID = "b93ac2c55b95518ae"

    def __init__(self, page = 1, res_num=5, country='pl'):
        self.start = (page - 1) * 10 + 1
        self.res_num = res_num
        self.country = country

    def search(self, query):
        url = f"https://www.googleapis.com/customsearch/v1?key={self.API_KEY}" \
              f"&cx={self.SEARCH_ENGINE_ID}&cr={self.country}" \
              f"&q={query}&start={self.start}&num={self.res_num}"

        data = requests.get(url).json()
        search_items = data.get("items")
        for i, search_item in enumerate(search_items, start=1):
            title = search_item.get("title")
            snippet = search_item.get("snippet")
            html_snippet = search_item.get("htmlSnippet")
            link = search_item.get("link")
            print("="*10, f"Result #{i+self.start-1}", "="*10)
            print("Title:", title)
            print("Description:", snippet)
            print("URL:", link, "\n")


# ga = GoogleApi()
# ga.search('inpost+pl')
