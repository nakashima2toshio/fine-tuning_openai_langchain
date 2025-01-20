#### https://console.anthropic.com/dashboard
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

#### Access to Claude 3 Haiku, our fastest model, and Claude 3 Opus

#### langchai - huggingface

| 機能名               | 関数名                                              | 説明                                                                                                                                                                                                 |
| -------------------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| モデルの統合         | HuggingFacePipeline<br> HuggingFaceTextGenInference | - Hugging Faceの様々な言語モデルをLangChainのパイプラインに統合<br>- テキスト生成、要約、翻訳などのタスクに対応したモデルを使用可能<br>- ローカルモデルや推論APIを利用したテキスト生成が可能         |
| トークナイザーの利用 | `HuggingFaceTokenizer`                              | - Hugging Faceのトークナイザーを使用して入力テキストを適切にトークン化<br>- モデルの入力形式に合わせたデータ前処理を容易に実行<br>- 異なるモデルに対応する様々なトークン化方法を提供                 |
| エンベディングの生成 | `HuggingFaceEmbeddings`                             | - Hugging Faceのモデルを使用してテキストのエンベディング（ベクトル表現）を生成<br>- 検索、類似度計算、クラスタリングなどのタスクに活用可能<br>- 様々な事前学習済みモデルからエンベディングを取得可能 |
| 質問応答             | `HuggingFaceQuestionAnswering`                      | - Hugging Faceの質問応答モデルをLangChainのチェーンに組み込み<br>- 文脈を考慮した高度な質問応答システムを構築可能<br>- 様々なドメインや言語に対応した質問応答を実現                                  |
| テキスト分類         | `HuggingFaceTextClassification`                     | - Hugging Faceの分類モデルを使用してテキストの分類タスクを実行<br>- センチメント分析、トピック分類、意図検出などに活用可能<br>- カスタムの分類タスクにも適用可能                                     |


### langchain
```python:langchain_huggingface.py
from langchain_huggingface import HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
model_id="microsoft/Phi-3-mini-4k-instruct",
task="text-generation",
pipeline_kwargs={
"max_new_tokens": 100,
"top_k": 50,
"temperature": 0.1,
},
)
llm.invoke("Hugging Face is")
```