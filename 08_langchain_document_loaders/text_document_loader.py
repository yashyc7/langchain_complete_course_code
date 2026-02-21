from langchain_community.document_loaders import TextLoader
from langchain_ollama import ChatOllama 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
loader = TextLoader('cricket.txt',encoding="utf-8")


document = loader.load()

print(document)
print(type(document)) #<class 'list'>

# [Document(metadata={'source': 'cricket.txt'},
#      page_content='The only time a software engineer truly understands “graceful shutdown” is when a well-set batsman gets out at 99.\n\nSystem running perfectly.\nNo errors.\nHigh performance.\n\nThen one unexpected edge to slip… and production is down.')]

#Now building simple rag below 

model = ChatOllama(model ="qwen2.5:3b-instruct-q4_K_M")
prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()
chain = prompt | model | parser

print(chain.invoke({"poem":document[0].page_content}))