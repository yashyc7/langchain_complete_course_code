from langchain_openai import (
    ChatOpenAI,
)  # not openai this time because we will using chat models
from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(model="gpt-4",temperature=0.3,max_completion_tokens=30) #tempreature controls deterministic and creativity while max_completion_token parameter controls the output token usage  , temperature varies between 0<->2.0 , 0 mean too deterministic or accurate while above 1 is used for creative tasks 

result = chat_model.invoke("what is the capital of india ? ")
print(result)
