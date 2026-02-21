#The contextual comprression reteriever in langchain is an advanced retriever that improves the retrieval quality by compressing documents after retrival keepign only the relevant content based on the user's query 

"""
Docstring for 5_contextual_compression_reterival
what is the photosynthesis ? 
the grand canyon is a famous natural sit. 
photosynthesis is how plants convert  light into energy many tourists visit every year . 


X Problem : 
the reteriver returns the entire paragraph . 
only one sentence is actually relevent to the query . 
the rest is the irrelevent noise that waastes context window and may confuse the llm . 

What contextual compression reteriver does ? 
returns only relevent part eg
photosynthesis is how plants convert light into energy .

How it works 

base reteriver eg faiss , chroma reterives N documents . 
a compresser then applied to each document . 
the compresse keeps only the parts relevent to the query . 
irrevelent content is discarded. 

When to Use: 
Your documents are long and contains mixed information 
You wanted to reduce context length of the llms 
you need to improve answer accuracy in RAG pipelines 

"""


from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_core.documents import Document
from langchain_ollama import ChatOllama
from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors import LLMChainExtractor



# Recreate the document objects from the previous data
docs = [
    Document(page_content=(
        """The Grand Canyon is one of the most visited natural wonders in the world.
        Photosynthesis is the process by which green plants convert sunlight into energy.
        Millions of tourists travel to see it every year. The rocks date back millions of years."""
    ), metadata={"source": "Doc1"}),

    Document(page_content=(
        """In medieval Europe, castles were built primarily for defense.
        The chlorophyll in plant cells captures sunlight during photosynthesis.
        Knights wore armor made of metal. Siege weapons were often used to breach castle walls."""
    ), metadata={"source": "Doc2"}),

    Document(page_content=(
        """Basketball was invented by Dr. James Naismith in the late 19th century.
        It was originally played with a soccer ball and peach baskets. NBA is now a global league."""
    ), metadata={"source": "Doc3"}),

    Document(page_content=(
        """The history of cinema began in the late 1800s. Silent films were the earliest form.
        Thomas Edison was among the pioneers. Photosynthesis does not occur in animal cells.
        Modern filmmaking involves complex CGI and sound design."""
    ), metadata={"source": "Doc4"})]


# Create a FAISS vector store from the documents
embedding_model = OllamaEmbeddings(model='all-minilm:latest')
vectorstore = FAISS.from_documents(docs, embedding_model)


base_retriever = vectorstore.as_retriever(search_kwargs={"k": 5})


# Set up the compressor using an LLM
llm = ChatOllama(model="qwen2.5:3b-instruct-q4_K_M")
compressor = LLMChainExtractor.from_llm(llm)

# Create the contextual compression retriever
compression_retriever = ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compressor
)

# Query the retriever
query = "What is photosynthesis?"
compressed_results = compression_retriever.invoke(query)

for i, doc in enumerate(compressed_results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)


# --- Result 1 ---
# Photosynthesis is the process by which green plants convert sunlight into energy.
