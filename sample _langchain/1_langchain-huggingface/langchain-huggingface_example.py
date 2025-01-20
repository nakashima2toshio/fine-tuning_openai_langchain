# pip install langchain-huggingface
# TOSHIO_API_KEY
# Anthropic: api_key = os.environ.get('TOSHIO_API_KEY')
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForCausalLM


class CodeGenerator:
    def __init__(self, model_name="meta-llama/CodeLlama-70b-Python-hf"):
        # モデルとトークナイザーの初期化
        self.prompt = None
        self.chain = None

        # Hugging Face pipelineの作成
        # ----------------------
        self.pipe = pipeline("text-generation", model="codellama/CodeLlama-70b-Python-hf")
        self.tokenizer = AutoTokenizer.from_pretrained("codellama/CodeLlama-70b-Python-hf")
        self.model = AutoModelForCausalLM.from_pretrained("codellama/CodeLlama-70b-Python-hf")
        # -----------------------

    def generate_code(self, task):
        # プロンプトテンプレートの定義
        self.prompt = PromptTemplate(
            input_variables=["task"],
            template="# Pythonで{task}関数を書いてください"
        )
        # LLMChainの作成
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)
        return self.chain.run(task)


def main():
    generator = CodeGenerator()
    task = "素数を判定する"
    generated_code = generator.generate_code(task)
    print(generated_code)


if __name__ == '__main__':
    main()
