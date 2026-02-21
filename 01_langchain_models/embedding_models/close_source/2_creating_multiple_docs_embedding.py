from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32) # 32 dimension vector in the output less dimension cost less tokens 

documents = ["delhi is the caital of india", "kolkata is the capital of west bengal","mumbai is the capital of the maharastra"]


#now performing actions like embed queries 


result= embedding.embed_documents(documents)

print(str(result)) # [[vector embeddings of 32 dimensions of first statement],[vector embeddings of 32 dimensions of second statement],[vector embeddings of 32 dimensions of third statement]]




