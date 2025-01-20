import os
import json
import requests
from bs4 import BeautifulSoup


class GradioFunctionScraper:
    def __init__(self):
        self.json_dir = './data/json/'
        self.json_path = os.path.join(os.getcwd(), self.json_dir)

    def get_function_name_and_url(self):
        # URLの設定
        url = "https://www.gradio.app/docs/gradio/interface"

        # ページの取得
        response = requests.get(url)

        # BeautifulSoupオブジェクトの作成
        soup = BeautifulSoup(response.content, 'html.parser')

        # a.thin-link要素の取得
        links = soup.select('a.thin-link.block')
        import pprint
        pprint.pprint(links)

        # リンクデータの作成
        links_data = {}
        for link in links:
            text = link.text.strip()
            href = link.get('href')
            if href and href.endswith('/') and text:
                links_data[text] = href

        for link in links:
            href = link.get('href')
            text = link.text.strip()
            if href and text:
                links_data[text] = href
        pprint.pprint(links_data)

        # JSONファイルの保存先を設定
        if not os.path.exists(self.json_path):
            os.makedirs(self.json_path)
        function_url_path = os.path.join(self.json_path, 'function_url.json')

        # JSONファイルとして保存
        with open(function_url_path, 'w') as json_file:
            json.dump(links_data, json_file, indent=4)

        return links_data


# 使用例
if __name__ == "__main__":
    scraper = GradioFunctionScraper()
    result = scraper.get_function_name_and_url()
    print(result)