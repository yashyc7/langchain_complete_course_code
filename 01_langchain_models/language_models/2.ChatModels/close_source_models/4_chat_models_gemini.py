from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
chat_model = ChatGoogleGenerativeAI(model="gemini-3-pro-preview")
result = chat_model.invoke("what is the capital of india ? ")
print(result)

