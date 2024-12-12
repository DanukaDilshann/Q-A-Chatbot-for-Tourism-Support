from langchain_huggingface import HuggingFaceEndpoint
import os
from langchain.prompts import PromptTemplate

sec_key = "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"
os.environ['HUGGINGFACEHUB_API_TOKEN'] = sec_key

repo_id = "microsoft/Phi-3-mini-4k-instruct"

llm = HuggingFaceEndpoint(repo_id=repo_id,temperature=0.7, max_length=128)
