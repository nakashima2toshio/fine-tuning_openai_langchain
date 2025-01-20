import json
import pprint

class ShowCode:
    def __init__(self, url_path):
        self.code_path = url_path

    def show_code_files(self):
        # JSONファイルを開いて読み込む
        with open(self.code_path, 'r', encoding='utf-8') as file:
            function_code = json.load(file)
            # pprint.pprint(function_code)


        # 辞書の各要素に対してループを実行
        for key, value in function_code.items():
            print('-----------------------')
            print('[{}] \n----------------------- {}'.format(key, value))


# JSONファイルのパス
code_path = './data/code/slider.json'
instance = ShowCode(code_path)
instance.show_code_files()
