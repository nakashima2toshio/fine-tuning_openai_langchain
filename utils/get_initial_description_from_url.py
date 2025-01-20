import requests
from bs4 import BeautifulSoup


def get_initial_description_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        print(html_content)
    else:
        html_content = ""
        print("Failed to retrieve the initial-data webpage")

    # beautifulsoupオブジェクトを作成する。
    # soup = BeautifulSoup(html_content, 'html.parse')
    soup = BeautifulSoup(html_content, 'lxml')

    initial_blocks = soup.find('tr', class_='group')

    return initial_blocks
