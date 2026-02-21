from langchain_ollama import ChatOllama

chat_model=  ChatOllama(model="qwen2.5:3b-instruct-q4_K_M")

chat_history  = []


while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result = chat_model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ",result.content)

print(chat_history)

#in langchain there are 3 messages 


#system_message 
#Human_message
#ai_message  