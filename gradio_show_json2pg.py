# gradio_show_json2pg.py
#
import os
import gradio as gr
import json
import logging

# JSONファイルが展開されたディレクトリのパス
cwd = os.getcwd()
directory_path = os.path.join(cwd, 'data/code/')
print(directory_path)
logger = logging.getLogger()


class ShowJson2PG:
    def __init__(self, directory_path):
        self.directory_path = directory_path

    # ファイル一覧を取得する関数
    def get_files_list(self):
        files = [f for f in os.listdir(self.directory_path) if os.path.isfile(os.path.join(self.directory_path, f))]
        return files

    # JSONファイルを読み込み、プログラム名とコードを返す関数
    def read_json_file(self, file_name):
        with open(os.path.join(self.directory_path, file_name), 'r') as file:
            data = json.load(file)
        programs = []
        for program_name, program_code in data.items():
            programs.append((program_name, program_code))
        return programs

    # ファイル選択と内容表示を処理する関数
    def display_programs(self, file_name):
        programs = self.read_json_file(file_name)
        outputs = []
        for program_name, program_code in programs:
            outputs.append(f"# Program Name: {program_name}\n# Program Code: ---------------------- \n{program_code}\n")
        # 余分なテキストボックスを空にするために追加
        while len(outputs) < 10:
            outputs.append("")
        return outputs


def main():
    instance = ShowJson2PG(directory_path)
    # ファイル一覧を取得
    files_list = instance.get_files_list()

    # グラディオのインターフェースを作成
    iface = gr.Interface(
        fn=instance.display_programs,
        inputs=gr.Dropdown(choices=files_list, label="Select a Function"),
        outputs=[gr.Textbox(label=f"Program {i + 1} Details", lines=10) for i in range(10)],  # 最大10個のプログラムを表示できるように設定
        title="Program Viewer"
    )

    # インターフェースを起動
    iface.launch()


if __name__ == "__main__":
    main()
