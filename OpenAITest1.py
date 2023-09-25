#import openai key
import os
os.environ['OPENAI_API_KEY']="#YOURKEYHERE"
#Import openai module from langchain
from langchain.llms import OpenAI
#temperature lies between 0 and 1, determines creativity of response
#default Open AI model is text-davinici-003
llm = OpenAI(temperature=0.7)
#give a prompt
prompt = "What would a good company name be for a consulting company that helps with engineering and tech?"
#models are here for OpenAI https://platform.openai.com/docs/models/overview
#print the prompt to Terminal with basic funtion ''print(llm(prmpt))''
#OR print a bunch using this:
result=llm.generate([prompt]*5)
for name in result.generations:
    print(name[0].text)
