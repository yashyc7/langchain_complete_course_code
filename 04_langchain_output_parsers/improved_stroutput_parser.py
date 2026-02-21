from langchain_ollama import ChatOllama 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 


chat_model = ChatOllama(model="qwen2.5:3b-instruct-q4_K_M")


template1= PromptTemplate(template="write a detailed report on {topic}",input_variables=["topic"])
template2 = PromptTemplate(template='write a 5 line summary on {text}',input_variables=['text'])




parser = StrOutputParser()
chain = template1 | chat_model | parser | template2 | chat_model | parser 

result = chain.invoke ({'topic':'computer',})

print(result)