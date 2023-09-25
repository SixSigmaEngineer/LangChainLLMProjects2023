#Prompt Templating and Chaining - Modular way to create prompts and Chaining Can allow you to chain template with LLM. Using "LLMChain" Variable from LangChain 
#import OpenAI API
from langchain.llms import OpenAI
from langchain.chains import LLMChain
#Pull in OpenAI API Key
import os
os.environ['OPENAI_API_KEY']='#YOURKEYHERE'
#From LangChain import promptemplate
from langchain import PromptTemplate
template1="You are a naming consultant for new secret projects. What is a good codeword for a client project that is in the busines of {product}? Make it one single codeword"
#generate a prompt by using template1 as a variable
prompt=PromptTemplate.from_template(template1)
#Choose OpenAI Model and Temperature
llm=OpenAI(temperature=0.9)
#initialize chain with parameters (chain,prompt)
#this chain will run on any specified product and call the LLM
chain=LLMChain(llm=llm, prompt=prompt)
#now print to terminal and define the business type or product type
print (chain.run("heart medical devices"))
