from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_ollama import ChatOllama




chat_template = ChatPromptTemplate(
    [
        SystemMessage(content = "You are a helpful {domain} expert"),
        HumanMessage(content="explain in simple terms what is {topic}")
    ]
)

prompt = chat_template.invoke ({'domain':'cricket','topic':'pitch'})

print(prompt)