# local_llama_python_chat.py
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory


class CodeLlamaChat:
    def __init__(self, model_path):
        print(f"Loading model from: {model_path}")
        print("This may take a while and require significant computational resources.")

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using device: {self.device}")

        # モデルとトークナイザーの初期化
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
            device_map="auto"
        )

        # Hugging Face pipelineの作成
        self.pipe = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            max_new_tokens=512,
            temperature=0.7,
            top_p=0.95,
            repetition_penalty=1.15
        )

        # LangChain HuggingFacePipelineの作成
        self.llm = HuggingFacePipeline(pipeline=self.pipe)

        # メモリの設定
        self.memory = ConversationBufferMemory()

        # ConversationChainの作成
        self.conversation = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            prompt=PromptTemplate(
                input_variables=["history", "input"],
                template="以下は人間とAIアシスタントの会話です。AIアシスタントは丁寧、創造的、賢明で、Pythonプログラミングに関する質問に答えることができます。\n\n会話履歴:\n{history}\n人間: {input}\nAIアシスタント: "
            )
        )

    def chat(self, user_input):
        return self.conversation.predict(input=user_input)


def main():
    model_path = "meta-llama/Meta-Llama-3-70B-Instruct"  # ローカルにダウンロードしたパスを指定
    chat_bot = CodeLlamaChat(model_path)

    print("チャットを開始します。終了するには 'quit' と入力してください。")
    while True:
        user_input = input("あなた: ")
        if user_input.lower() == 'quit':
            break
        response = chat_bot.chat(user_input)
        print("AIアシスタント:", response)


if __name__ == "__main__":
    main()