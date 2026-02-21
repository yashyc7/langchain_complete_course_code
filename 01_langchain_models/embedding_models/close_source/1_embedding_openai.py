from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()


embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32) # 32 dimension vector in the output less dimension cost less tokens 

#now performing actions like embed queries 


result= embedding.embed_query("Delhi is the capital of india")

print(str(result)) #[vector embeddings of 32 dimensions of first statement]




