from langchain_ollama import ChatOllama

chat_model = ChatOllama(model="qwen2.5-coder:7b")

result = chat_model.invoke("what is your name ? ")

print(result.content)
