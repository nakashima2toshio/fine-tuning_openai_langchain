# (1) crawl_function_url2json.py by selenium
# crawl_function_html2files.py
# brew install chromedriver
import os
import json
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from crawl_python_code import CrawlerPythonCode
import pprint


class CrawlerCode:
    def __init__(self):
        self.json_dir = './data/json/'
        self.html_dir = 'data/html/'
        self.json_path = os.path.join(os.getcwd(), self.json_dir)
        self.html_path = os.path.join(os.getcwd(), self.html_dir)

    def first_letter_big(self, text: str) -> str:
        if text:
            return text[0].upper() + text[1:]
        return text

    def get_function_name_and_url(self):
        if not os.path.exists(self.json_path):
            os.makedirs(self.json_path)
        function_url_path = os.path.join(self.json_path, 'function_url.json')

        s = Service('/opt/homebrew/bin/chromedriver')  # ここにchromedriverの絶対パスを指定
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # ヘッドレスモードを有効化
        driver = webdriver.Chrome(service=s, options=options)

        try:
            # GradioのWebページにアクセス
            driver.get("https://www.gradio.app/docs/gradio")

            # ページが完全にロードされるのを待つ
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.sidebar-content a.thin-link')))

            # JavaScriptの実行を待つ
            time.sleep(2)

            # より具体的なCSSセレクタを使用
            links = driver.find_elements(By.CSS_SELECTOR, 'div.sidebar-content a.thin-link')

            links_data = {}
            for link in links:
                text = link.text.strip()
                href = link.get_attribute('href')
                if href and href.endswith('/') and text:
                    links_data[text] = href

            pprint.pprint(links_data)

            # JSONファイルとして保存
            with open(function_url_path, 'w') as json_file:
                json.dump(links_data, json_file, indent=4)

        except Exception as e:
            print(f"エラーが発生しました: {e}")

        finally:
            driver.quit()

        # return links_data

    def get_docs_url_by_selenium(self):
        # ディレクトリの確認と作成、ディレクトリが存在しない場合は作成
        if not os.path.exists(self.json_path):
            os.makedirs(self.json_path)

        # function_name: function_url.jsonファイルのパス
        function_url_path = os.path.join(self.json_path, 'function_url.json')

        # ChromeDriverのパスをServiceオブジェクトとして指定
        s = Service('/opt/homebrew/bin/chromedriver')  # ここにchromedriverの絶対パスを指定
        driver = webdriver.Chrome(service=s)

        # GradioのWebページにアクセス
        driver.get("https://www.gradio.app/docs/gradio")
        # ページが完全にロードされるのを待つために少し待つ
        time.sleep(3)
        # 遷移後のページ内のすべてのリンクを取得

        # <a class="thin-link px-4 block leading-8" href="group">Group</a>
        # <button class="demo-btn px-4 py-2 text-lg min-w-max text-gray-600 hover:text-orange-500 selected-demo-tab" name="blocks_hello">blocks_hello</button>
        # <gradio-lite playground shared-worker layout="vertical" class="p-2">i
        # CSSセレクタを使用して"Docs"リンクを見つける
        # docs_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="interface"]'))
        # )
        # docs_button.click()

        # ページが完全にロードされるのを待つために少し待つ
        time.sleep(3)

        # 遷移後のページ内のすべてのリンクを取得
        links = driver.find_elements(By.CSS_SELECTOR, 'a.thin-link')
        pprint.pprint(links)
        # リンクのテキストとURLの一覧を表示
        links_data = {}
        for link in links:
            text = link.text
            href = link.get_attribute('href')
            if href[-1] == '/':
                links_data[text] = href

        pprint.pprint(links_data)

        # JSONファイルとして保存
        with open(function_url_path, 'w') as json_file:
            json.dump(links_data, json_file, indent=4)

        driver.quit()

    def json2html_file(self):
        # ../data/json/links_data.jsonを読み込み、links_dataにdict型で格納する
        links_data = {}
        with open('data/json/function_url.json', 'r', encoding='utf-8') as file:
            links_data = json.load(file)

        # links_data.json からkey, value=URLを取り出して、
        # key + '.html'のファイル名で、../data/html/ に保存する
        for key, value in links_data.items():
            # ファイルパス
            file_path = os.path.join(self.html_dir, f'{key}.html')
            # valueのURLからHTMLを読み込み
            html_content = requests.get(value).text
            # 読み込んだHTMLをBeautiful Soupで解析して
            soup = BeautifulSoup(html_content, 'html.parser')
            # ファイルに書き込み
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(soup.prettify())

    def crawler_get_code(self):
        # function_url.jsonの読み込み
        with open('./data/json/function_url.json', 'r') as fp:
            function_url_data = json.load(fp)
        # for function_name, function_url in function_url_data.items():
        #     print('[{}] -> [{}]'.format(function_name, function_url))
        # print('-------------------')
        # python-codeを取り出し、functionごとのファイルを作成する。
        for function_name, function_url in function_url_data.items():
            print('[{}] -> [{}]'.format(function_name, function_url))
            code_dic = {}
            # print(f'html_dir: {self.html_dir}')
            # HTMLファイルの読み込み
            parsed_url = urlparse(function_url)
            parsed_path = parsed_url.path.rstrip('/')  # 末尾のスラッシュを削除
            function_component_0 = parsed_path.split('/')[-1]  # 一番後ろのURL-コンポーネント
            function_component = self.first_letter_big(function_component_0)

            html_file_path = os.path.join(self.html_path, f'{function_component}.html')
            print(f'html_file_path= {html_file_path}')

            if not os.path.exists(html_file_path):
                print(f"The file {html_file_path} does not exist. Please check the path.")
                break
            with open(html_file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()

            soup = BeautifulSoup(html_content, 'html.parser')
            div_class = "codeblock"  # 抽出したいdivのクラス名
            divs = soup.find_all("div", {"class": div_class})
            print('divs------------->', divs)

            # print(function_url)
            # Pythonコードの抽出
            crawler = CrawlerPythonCode(function_url)
            code_blocks = crawler.get_python_code(divs)
            example_code = crawler.get_example_code(divs)
            if example_code is None:
                example_code = {}
            code_dic.update(code_blocks)
            code_dic.update(example_code)

            pprint.pprint(code_dic)
            file_name = os.path.join('data/code/', f'{function_name}.json')
            os.makedirs(os.path.dirname(file_name), exist_ok=True)  # ディレクトリが存在しない場合は作成
            with open(file_name, 'w') as f:
                f.write(json.dumps(code_dic, ensure_ascii=False, indent=4))

    def run(self):
        self.get_function_name_and_url()  # json-file
        # self.json2html_file()  # html-files
        # self.crawler_get_code()  # code-files
        print("Processing complete.")


def main():
    crawler = CrawlerCode()
    crawler.run()


if __name__ == "__main__":
    main()
