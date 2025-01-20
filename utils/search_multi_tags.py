import requests
from bs4 import BeautifulSoup
import autopep8


def search_multi_tags(self, url, tag):
    # url = "https://www.gradio.app/docs/slider/"
    self.class_tag = tag
    self.response = requests.get(url)

    # ステータスコードが200であることを確認（成功したリクエスト）
    if self.response.status_code == 200:
        html_content = self.response.text
    else:
        print("Failed to retrieve the webpage")
        html_content = ""

    # BeautifulSoupオブジェクトを作成
    self.soup = BeautifulSoup(html_content, 'html.parser')

    # soupはBeautifulSoupオブジェクトを指しています。HTMLドキュメントがパースされたものです。
    divs = self.soup.find_all("div", {"class": self.class_tag})
    self.id_tag_code = dict()
    self.div_id_lst = {}
    self.div_id_no = 0
    for i, div in enumerate(divs, start=1):
        self.div_id_title = div.get("id")
        if self.div_id_title is not None:
            self.div_id_lst[self.div_id_no] = self.div_id_title
            self.div_id_no += 1
            print('div ------> ', self.div_id_title)

            # このdiv内のすべてのclassが"code language-python"のcodeタグを検索
            self.code_blocks = div.find_all("code", {"class": "code language-python"})
            for j, code_block in enumerate(self.code_blocks, start=1):
                python_code = code_block.text
                formatted_code = autopep8.fix_code(python_code)
                self.id_tag_code[id] = formatted_code

    return self.id_tag_code, self.div_id_lst