# div id="description" 以下を抽出する。
import json
import pprint
from crawl_description_strings import CrawlerDescriptionStrings


class CrawlerDescription:

    def crawler_get_description(self):
        # function_url.jsonの読み込み
        with open('./data/json/function_url.json', 'r') as fp:
            function_url_data = json.load(fp)

        function_description_data = dict()
        # function_descriptionを取り出し、functionごとのファイルを作成する。
        for function_name, function_url in function_url_data.items():
            txt = CrawlerDescriptionStrings(function_url).run()
            function_description_data[function_name] = txt.replace("\t", '')
        return function_description_data


instance = CrawlerDescription()
function_description_data = instance.crawler_get_description()
# for function_name, description in function_description_data.items():
#     print('[{}]: {}\n'.format(function_name, description))
with open('data/description/description.json', 'w') as fp:
    json.dump(function_description_data, fp)
