# Gradioから、Pythonコードを抽出するメインプログラム
# (1) タグ名: URIのDemoプログラムを抜き出す。
# (2-1) タグ名: URIの 情報を抜き出す。
# (2-2) 抜き出した情報(プログラム)を保存する。
#       ------ここまで。
# (3-1) [GPT-4] 取得したデータで、Fine-Tuning用のデータを作成
# (3-2) [GptForAll] [GPT-4] 取得したデータで、Fine-Tuning用のデータを作成
# (4-1) [GPT-4] 取得したデータで、Fine-Tuning する。
# (4-2) [GptForAll-Local] 取得したデータで、Fine-Tuning する。
# (5) 利用評価
import os
import json
import requests
from bs4 import BeautifulSoup
import pprint

from crawl_python_code import CrawlerPythonCode  # 追加: 必要なモジュールをインポート


class CrawlerCode:
    def __init__(self):
        self.json_dir = './data/json/'
        self.json_path = os.path.join(os.getcwd(), self.json_dir)

    def get_submenu_to_json_path(self):
        # ディレクトリの確認と作成、ディレクトリが存在しない場合は作成
        if not os.path.exists(self.json_path):
            os.makedirs(self.json_path)

        # function_name: function_url.jsonファイルのパス
        function_url_path = os.path.join(self.json_path, 'function_url.json')

        # GradioのWebページにアクセス
        url = "https://www.gradio.app/docs/gradio/interface"
        response = requests.get(url)
        response.raise_for_status()  # リクエストが成功したか確認

        # BeautifulSoupを使用してHTMLをパース
        soup = BeautifulSoup(response.text, 'html.parser')

        # 遷移後のページ内のすべてのリンクを取得
        links = soup.select('a.thin-link')

        # リンクのテキストとURLの一覧を表示
        links_data = {}
        base_url = "https://www.gradio.app/docs/gradio/"

        for link in links:
            function_name = link.get_text(strip=True)
            function_url = link.get('href')
            if function_url and not function_url.startswith("http"):
                function_url = base_url + function_url
            links_data[function_name.lower()] = function_url

        # pprint.pprint(links_data)
        # jsonファイルとして保存
        with open(function_url_path, 'w') as file:
            json.dump(links_data, file, ensure_ascii=False, indent=4)

        print(f"リンクデータは '{function_url_path}' に保存されました。")

        # ブラウザを閉じる
        return True

    def crawler_get_code(self):
        # [function_url.json] GradioのURL：サブメニューから、サブメニュー：URL　のデータ　
        # self.get_submenu_to_json_path()

        # function_url.jsonの読み込み
        with open('data/json/function_url.json', 'r') as fp:
            function_url_data = json.load(fp)

        pprint.pprint(function_url_data)
        # python-codeを取り出し、functionごとのファイルを作成する。
        for function_name, function_url in function_url_data.items():
            print('[{}] -> [{}]'.format(function_name, function_url))

            # python codeの取り出し
            crawler = CrawlerPythonCode(function_url)
            div_class = "codeblock"  # 抽出したいdivのクラス名
            code_blocks = crawler.run(div_class)
            function_name = function_url.split("/")[-2]  # function名を抽出する。

            file_name = 'data/code/' + function_name + '.json'
            os.makedirs(os.path.dirname(file_name), exist_ok=True)  # ディレクトリが存在しない場合は作成
            with open(file_name, 'w') as f:
                f.write(json.dumps(code_blocks))


def main():
    instance = CrawlerCode()
    instance.crawler_get_code()


if __name__ == "__main__":
    main()
