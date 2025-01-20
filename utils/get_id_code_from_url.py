# get_idcode_from_url.py
import requests
from bs4 import BeautifulSoup, ResultSet
import autopep8
from typing import Dict, Tuple, Callable, Any


def fetch_html(self, url: str) -> requests.Response:
    self.response = requests.get(url)
    if self.response.status_code != 200:
        print("Failed to retrieve the webpage")
        response = None
    return self.response


def extract_divs(self, response: requests.Response, div_class: str):
    self.html_content = response.text if response else ""
    self.soup = BeautifulSoup(self.html_content, 'html.parser')
    self.divs = self.soup.find_all("div", {"class": div_class})
    return self.divs


def get_python_code(self, divs: BeautifulSoup) -> tuple[dict[int, Any], dict[Callable[[object], int], Any]]:
    self.id_code_json = dict()
    self.div_id_list = {}
    self.div_id_no = 0
    for i, div in enumerate(divs, start=1):
        self.div_id_title = div.get("id")
        if self.div_id_title is not None:
            self.div_id_list[self.div_id_no] = self.div_id_title
            self.div_id_no += 1
            self.code_blocks = div.find_all("code", {"class": "code language-python"})
            for j, code_block in enumerate(self.code_blocks, start=1):
                python_code = code_block.text
                formatted_code = autopep8.fix_code(python_code)
                self.id_code_json[id] = formatted_code

    return self.div_id_list, self.id_code_json
