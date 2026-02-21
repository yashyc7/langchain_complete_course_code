from langchain_openai import (
    ChatOpenAI,
)  # not openai this time because we will using chat models
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(model="gpt-4")
result = chat_model.invoke("what is the capital of india ? ")
print(result)
