#Use Human Input to Generate Codename via OpenAI API

#Pull in OpenAI API Key
import os
os.environ['OPENAI_API_KEY']='#YOUR KEY HERE'

#import OpenAI API and LLMChain
from langchain.llms import OpenAI
from langchain.chains import LLMChain

#From LangChain import promptemplate
from langchain import PromptTemplate
template1="What is a good codeword for a client project that is in the busines of {product}? Make it one single codeword."

#generate a prompt by using template1 as a variable
prompt=PromptTemplate.from_template(template1)

#Choose OpenAI Model and Temperature
llm=OpenAI(temperature=0.8)

#initialize chain with parameters (chain,prompt)
#this chain will run on any specified product and call the LLM
chain=LLMChain(llm=llm, prompt=prompt)

#input from human
var=input("please enter something:")

#now print to terminal and define the business type or product type
print (chain.run(var))
