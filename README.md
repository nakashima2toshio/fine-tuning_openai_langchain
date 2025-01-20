### ローカルのLLM（モデル）へFine-Tuningを実施し、性能評価する（作成中）
- Fine-Tuning用トレーニングデータを作成する。
  - 対象：(Hugging FaceのGradio(フレームワーク)をクロールしデータを収集する)
    - クロールで、Gradioの「サンプルプログラム」の収集する。
    - クロールで、Gradioの「それぞれの機能仕様書」の収集する。
    - クロールで、Gradioの「それぞれの機能をHTMLで」の収集し、PDFに変換する。（←いまここ）
  - 収集データを『Hugging FaceのTransformersツール等で』訓練用データに変換する
- ローカルのLLMを訓練する。（Fine-Tuningする）
- ローカルのLLMで、プログラムを生成する。(LangChain, Transformerを利用)
- 同上と同一のスクリプトで、CharGPT4oのAPIで、プログラムを生成する。
- 成果を比較する。
* 目標
1. Transformersツールを利用する。Transformerのスクラッチでも実装し、比較したい。
2. Fine-Tuning用トレーニングデータの作成。
3. Fine-Tuningを実施する。
4. ChatGPT-4へのFine-Tuningと評価
5. GPT4oへのFine-Tuningと評価
6. llama-Index, langChain, LoLa
7. 

a. 任意のURLからスクレイピング（Webページからデータを抽出：特定のデータ構造）し訓練データを作成する。
   a1. クロール単位で（HTMLのAタグを解析しておいて：事前に）
　　a1. Gragioの技術情報から、Q&A, Q&Programing_Exampleのモデル・追加・訓練用のデータが欲しい。

* LLM: Language Learning Model
  * [LLM](大規模言語モデル）への追加学習
    * Prompting: プロンプト
    * LoLA (Alpaca-LoRA):
    * PEFT
  * Alpaca-LoRA

* Fine-tuning: PEFT-RoLA by PyTorch (追加学習)
  * GPT4: ChatGPT by OpenAI, HuggingFace
  * Codel Llama - Python：Pythonに特化したモデル
  * GPT3: ELYZA-japanese-Llama-2-13B
  * GPT3: Falcon by HuggingFace

* 株価表示 gradio + FastAPI

  1. 必要なライブラリをインポートします。
  2. Yahoo Finance APIを使用して株価データを取得する関数を定義します。
  3. matplotlibを使用して株価のグラフを作成する関数を定義します。
  4. Gradioインターフェースを定義し、ユーザーが証券コードを入力できるようにします。
  5. FastAPIを使用してサーバーを起動します。

* LangChain

1. memory
2. aaa
3. bbb

* Hugging Face
  * Models
    * text-generation
  * 
    * [Hugging Face](https://huggingface.co/)
    * Hugging Face Models
      * Hugging Face Tokenizers
      * Hugging Face Accelerate
      * Hugging Face Trainer
      * Hugging Face Examples
      * Hugging Face Datasets
    
    * Hugging Face Transformers　・・・　ライブラリー
    * Hugging Face Pipelines　　　・・・　モデルを使ってみる
 
  
* Docker環境を作成し、PyCharmで開発できるようにする。
* setup
$ git clone git@github.com:nonamenme/docker-fastapi-postgres.git
$ cd docker-fastapi-postgres
$ cp .env.example .env

### Fine Tuning
