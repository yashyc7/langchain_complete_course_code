from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity


embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",model_kwargs = {"device": "cpu"})


documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]


query = ' tell me about dhoni '

docs_vectors = embedding.embed_documents(documents) #2d list 

query_vector = embedding.embed_query(query) #1d list 


print(cosine_similarity([query_vector],docs_vectors)) # here we provide the 2d vectors thats why wrapping query into one more brackets

#scores = cosine_similarity([query_vector],docs_vectors)[0] #since it returns the 2d array so we access its first element [[0.8177796  0.42080611 0.48464816 0.50567356 0.37444926]] -> [0.8177796  0.42080611 0.48464816 0.50567356 0.37444926]

scores = cosine_similarity([query_vector], docs_vectors)[0]

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is:", score)