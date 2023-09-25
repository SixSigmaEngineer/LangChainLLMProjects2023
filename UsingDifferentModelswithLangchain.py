#How to use different LLM Models with LangChain
#First import HuggingFace Key
import os
os.environ['HUGGINGFACEHUB_API_TOKEN']="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"
#Import HuggingFace module from LangChain
from langchain import HuggingFaceHub
#Make a new instance with Model from HuggingFace
llm=HuggingFaceHub(repo_id="google/flan-t5-base",model_kwargs={"temperature":0, "max_length":64})
#model kwargs are the settings for the model
#now give a prompt
prompt="What are good fitness tips?"
#simply print the llm prompt in terminal
print(llm(prompt))