import requests
from bs4 import BeautifulSoup


def get_code_from_url(url):
    # url = "https://www.gradio.app/docs/slider/"
    response = requests.get(url)

    # ステータスコードが200であることを確認（成功したリクエスト）
    if response.status_code == 200:
        html_content = response.text
    else:
        print("Failed to retrieve the webpage")
        html_content = ""

    # BeautifulSoupオブジェクトを作成
    soup = BeautifulSoup(html_content, 'html.parser')

    # 特定のdivをidで検索
    codeblock_div = soup.find("div", {"class": "demo-content"})

    code_id_text = dict()
    # codeblock_divがNoneでないことを確認
    if codeblock_div:
        # div内のすべてのcodeblockを検索
        code_blocks = codeblock_div.find_all("div", {"class": "codeblock"})

        for code_block in code_blocks:
            # codeblockのidを表示
            print(code_block.get("id"))
            id_name = code_block.get("id")
            txt = code_block.get("text")
            # codeblockのテキスト内容を表示
            print(code_block.text)
            code_id_text[id_name] = txt
        return code_id_text
    else:
        print("The specified div was not found")
        return '-'  # None

