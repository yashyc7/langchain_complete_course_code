#mmr is an information reterival algorithm designed to reduce
# redundancy in the reterived results while maintaining the high relevence to the query

# how can e pick resluts that ar enot only relevent to the query 
# but also different from each other ?

# we use it to reduce redundancy also  

# Sample documents

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

embedding_model = OllamaEmbeddings(model='all-minilm:latest')

vector_store = FAISS.from_documents(documents=docs, embedding=embedding_model)


# Enable MMR in the retriever
retriever = vector_store.as_retriever(
    search_type="mmr",                   # <-- This enables MMR
    search_kwargs={"k": 3, "lambda_mult": 0.5}  # k = top results, lambda_mult = relevance-diversity balance
)

query = "What is langchain?"
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)



# --- Result 1 ---
# LangChain supports Chroma, FAISS, Pinecone, and more.

# --- Result 2 ---
# LangChain is used to build LLM based applications.

# --- Result 3 ---
# Embeddings are vector representations of text.