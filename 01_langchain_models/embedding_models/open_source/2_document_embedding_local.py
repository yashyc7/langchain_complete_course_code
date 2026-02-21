from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",model_kwargs = {"device": "cpu"})
documents = ["delhi is the caital of india", "kolkata is the capital of west bengal","mumbai is the capital of the maharastra"]


#now performing actions like embed queries 


result= embedding.embed_documents(documents)

print(str(result)) # [[vector embeddings of 32 dimensions of first statement],[vector embeddings of 32 dimensions of second statement],[vector embeddings of 32 dimensions of third statement]]
