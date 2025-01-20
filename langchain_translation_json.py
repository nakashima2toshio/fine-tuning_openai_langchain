"""
'../data/description/description.json' データを読み込み、
description.jsonのkeyデータを「Gradio関数名」とし、valueをその「関数の説明」としている。
open_aiのapiとlangchainを利用して、
「Gradio関数名」と「関数の説明」を日本語化し、かつ、関数の説明のないものは、
open_aiを利用して、説明を入れ、
description.jsonの日本語版である：description_j.jsonを作成せよ。
"""
import os
import json
import re
# from typing import re

import autopep8
import openai

from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain, LLMChain
from langchain.llms import OpenAI
import pprint

from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

from utils.read_write_file import ReadWriteFile


class LanguageChainTranslationJson(object):
    def __init__(self):
        self.description_e_path = os.path.join('./data/description/', 'description.json')
        self.description_j_path = os.path.join('./data/description/', 'description_j.json')
        self.description_e = ReadWriteFile(self.description_e_path)  # 初期化しただけ
        self.description_j = ReadWriteFile(self.description_j_path)
        self.data_j_dict = dict()
        self.data_e_dict = dict()
        self.template = PromptTemplate()
        self.openai_api_key = os.environ.get("OPEN_AI_API_KEY")
        self.chat_model_name = 'gpt-3.5-turbo-instruct'

    # '../data/description/description_j.json'ファイルを読み込みjsonとして返却する
    def description_json_e(self):
        with open(self.description_e_path, 'r') as fp:
            return json.load(fp)

    def description_json_j(self):
        with open(self.description_j_path, 'r') as fp:
            return json.load(fp)

    def show_description_e(self):
        for key, value in self.description_json_e().items():
            print('------------------------')
            print('[{}] - {}'.format(key, value))

    def show_description_j(self):
        for key, value in self.description_json_j().items():
            print('[{}] - {}'.format(key, value))

    def show_question_e(self):
        count = 0
        for key, value in self.description_json_e().items():
            if key == 'Slider':
                instruction = 'あなたは、プログラミング、python、Gradioをプロのソフトウエア技術者にコーディングに必要な情報を整理して、日本語でわかりやすく教えることができる。'
                instruction += 'Gradioの{key}機能の概要、引数の一覧をmd形式の表で説明してほしい。'.format(key=key)
                print('[{key}]\n- {instruction}'.format(key=key, instruction=instruction, value=value))
                chat = ChatOpenAI(
                    openai_api_key=self.openai_api_key,
                    model='gpt-4-0125-preview'
                )
                # --- メッセージを指定(プロンプト) ---
                messages = [
                    HumanMessage(content=instruction),
                ]
                # --- 実行: メソッドを指定 ---
                response = chat.invoke(messages)
                print('[{key}]---{response}'.format(key=key, response=response))
                count = count + 1
                if count > 2:
                    break

    def show_openapi_completion(self):
        #
        instruction = 'あなたは、プログラミング、python, Gradioをわかりやすく教えることができる。'
        key = 'GradioのSlider機能と、使い方例のプログラムも添付して日本語で説明して'
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": instruction},
                {"role": "user", "content": key},
            ],
            max_tokens=100,
            n=1,
            temperature=0.7,
        )

    def gpt4_to_gpt35(self, instruction):
        llm = OpenAI(openai_api_key=self.openai_api_key, temperature=0.9, model=self.chat_model_name)
        self.template = instruction
        prompt = PromptTemplate.from_template(self.template)
        # ユーザー入力に基づいてプロンプトを定義
        question = "あなたは、プログラミング、pythonをわかりやすく日本語で説明できます。"
        question += "GradioのSilder機能のを概要、引数の一覧、使い方例のプログラムも添付して日本語で説明してください。"

        # LLMチェーンの作成と実行
        llm_chain = LLMChain(llm=llm, prompt=prompt)
        result = llm_chain.run(question)
        pprint.pprint(result)

    def chatgpt4_response(self):
        # --- 初期化: モデルを指定 ---
        chat = ChatOpenAI(
            openai_api_key=self.openai_api_key,
            model='gpt-4-0125-preview'
        )
        content = ("Gradioの{function_name}機能を詳しく、わかり易く日本語で説明して。")
        content += "わかり易くするために、プログラム例を使って説明してね。"
        # --- メッセージを指定(プロンプト) ---
        messages = [
            HumanMessage(content=content),
        ]

        # --- 実行: メソッドを指定 ---
        response = chat.invoke(messages)
        # formatted_code = autopep8.fix_code(python_code)
        print(response.content)
        # 正規表現パターンで'''で囲まれた部分を抽出
        codes = re.search(r"'''(.*)'''", response.content)
        formatted_code = autopep8.fix_code(codes)
        print(formatted_code)


instance = LanguageChainTranslationJson()
instance.show_question_e()
