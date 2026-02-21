#sometimes a single query  must not captuere all the wayus information is pharsed in your documents 
"""
for eg. 
query : 
how can i stay healthy? 


could mean : 
what should i eat ? 
how often should i exersice ? 
how can i manage stress? 

a simple similarity search might miss documents that talk about those 
things but dont use word 'healthy' 


how does it work : 

1. takes your original query 

2. use an llm (eg. 3.5 )to geneate multiple semantically differnt  verisons of that query 

3. perform retrival for each sub query 

4.  combines and deduplicates the result s

"""

from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document
from langchain_ollama import ChatOllama
from langchain_classic.retrievers.multi_query import MultiQueryRetriever




# Relevant health & wellness documents
all_docs = [
    Document(page_content="Regular walking boosts heart health and can reduce symptoms of depression.", metadata={"source": "H1"}),
    Document(page_content="Consuming leafy greens and fruits helps detox the body and improve longevity.", metadata={"source": "H2"}),
    Document(page_content="Deep sleep is crucial for cellular repair and emotional regulation.", metadata={"source": "H3"}),
    Document(page_content="Mindfulness and controlled breathing lower cortisol and improve mental clarity.", metadata={"source": "H4"}),
    Document(page_content="Drinking sufficient water throughout the day helps maintain metabolism and energy.", metadata={"source": "H5"}),
    Document(page_content="The solar energy system in modern homes helps balance electricity demand.", metadata={"source": "I1"}),
    Document(page_content="Python balances readability with power, making it a popular system design language.", metadata={"source": "I2"}),
    Document(page_content="Photosynthesis enables plants to produce energy by converting sunlight.", metadata={"source": "I3"}),
    Document(page_content="The 2022 FIFA World Cup was held in Qatar and drew global energy and excitement.", metadata={"source": "I4"}),
    Document(page_content="Black holes bend spacetime and store immense gravitational energy.", metadata={"source": "I5"}),
]


# Initialize OpenAI embeddings
embedding_model = OllamaEmbeddings(model='all-minilm:latest')

# Create FAISS vector store
vectorstore = FAISS.from_documents(documents=all_docs, embedding=embedding_model)


# Create retrievers
similarity_retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})


multiquery_retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(search_kwargs={"k": 5}),
    llm=ChatOllama(model="qwen2.5:3b-instruct-q4_K_M")
)

# Query
query = "How to improve energy levels and maintain balance?"

# Retrieve results
similarity_results = similarity_retriever.invoke(query)
multiquery_results= multiquery_retriever.invoke(query)


for i, doc in enumerate(similarity_results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)

print("*"*150)

for i, doc in enumerate(multiquery_results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)



# --- Result 1 ---
# Drinking sufficient water throughout the day helps maintain metabolism and energy.

# --- Result 2 ---
# The solar energy system in modern homes helps balance electricity demand.

# --- Result 3 ---
# Consuming leafy greens and fruits helps detox the body and improve longevity.

# --- Result 4 ---
# Mindfulness and controlled breathing lower cortisol and improve mental clarity.

# --- Result 5 ---
# Photosynthesis enables plants to produce energy by converting sunlight.
# ******************************************************************************************************************************************************

# --- Result 1 ---
# Drinking sufficient water throughout the day helps maintain metabolism and energy.

# --- Result 2 ---
# The solar energy system in modern homes helps balance electricity demand.

# --- Result 3 ---
# Consuming leafy greens and fruits helps detox the body and improve longevity.

# --- Result 4 ---
# Photosynthesis enables plants to produce energy by converting sunlight.

# --- Result 5 ---
# Mindfulness and controlled breathing lower cortisol and improve mental clarity.

# --- Result 6 ---
# Regular walking boosts heart health and can reduce symptoms of depression.
# PS C:\Users\pc\Desktop\langchain_retrievers> 