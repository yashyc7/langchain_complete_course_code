from langchain_ollama import ChatOllama 
from langchain_core.prompts import PromptTemplate 


chat_model = ChatOllama(model="qwen2.5:3b-instruct-q4_K_M")


template1= PromptTemplate(template="write a detailed report on {topic}",input_variables=["topic"])
template2 = PromptTemplate(template='write a 5 line summary on {text}',input_variables=['text'])


prompt1 = template1.invoke({'topic':"computer"})

result = chat_model.invoke(prompt1)

prompt2 = template2.invoke({"text":result.content})


result = chat_model.invoke(prompt2)

print(result.content )