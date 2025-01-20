import json
import pprint


class ShowDescription(object):
    def __init__(self, file_path):
        self.description_path = file_path

    def show_description_file(self):
        # JSONファイルを開いて読み込む
        with open(self.description_path, 'r', encoding='utf-8') as file:
            function_description = json.load(file)

        # 辞書の各要素に対してループを実行
        for key, value in function_description.items():
            print('-----------------------')
            print('[{}] \n----------------------- {}\n'.format(key, value))

    def show_keys(self):
        with open(self.description_path, 'r') as fk:
            function_description = json.load(fk)
            print('len= ', len(function_description.keys()))
            for key, value in function_description.items():
                if value == 'No description found.':
                    print('[{}] \n[{}]'.format(key, value))


# JSONファイルのパス
description_path = './data/description/description.json'
instance = ShowDescription(description_path)
instance.show_keys()
