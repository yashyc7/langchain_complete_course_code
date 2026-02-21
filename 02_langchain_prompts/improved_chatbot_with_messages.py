from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

chat_model=  ChatOllama(model="qwen2.5:3b-instruct-q4_K_M")

chat_history  = [
SystemMessage(content="Your name is Yash chauhan not qwen and you are helpful ai assistant"),

]


while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(user_input))
    if user_input == 'exit':
        break
    result = chat_model.invoke(chat_history)
    chat_history.append(AIMessage(result.content))
    print("AI: ",result.content)

print(chat_history)
