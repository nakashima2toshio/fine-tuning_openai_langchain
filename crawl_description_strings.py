
#
from typing import Any, Callable, Dict, List, Optional
import requests
from bs4 import BeautifulSoup


class CrawlerDescriptionStrings(object):
    def __init__(self, url: str):
        self.div_name = ''
        self.id_description_json = None
        self.url = url
        self.response = None
        self.soup = None

    def fetch_html(self) -> Optional[requests.Response]:
        self.response = requests.get(self.url)
        if self.response.status_code != 200:
            print("Failed to retrieve the webpage")
            return None
        return self.response

    def get_description_string(self) -> str:
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        description_div = self.soup.find('div', id='description')
        if description_div is not None:
            description_text = description_div.get_text()
        else:
            description_text = ''  # "No description found."
        return description_text.strip()

    def run(self) -> str:
        self.fetch_html()
        return self.get_description_string()

#
# url_data = 'https://www.gradio.app/docs/slider/'
# instance = CrawlerDescriptionStrings(url_data)
# msg = instance.run()
# print(msg)
