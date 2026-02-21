#its an opensource database 
from langchain_ollama import OllamaEmbeddings

from langchain_classic.schema import Document

from langchain_chroma import Chroma

embed_model = OllamaEmbeddings(model='all-minilm:latest')


doc1 = Document(
        page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
        metadata={"team": "Royal Challengers Bangalore"}
    )
doc2 = Document(
        page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
        metadata={"team": "Mumbai Indians"}
    )
doc3 = Document(
        page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
        metadata={"team": "Chennai Super Kings"}
    )
doc4 = Document(
        page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
        metadata={"team": "Mumbai Indians"}
    )
doc5 = Document(
        page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
        metadata={"team": "Chennai Super Kings"}
    )


docs = [doc1,doc2,doc3,doc4,doc5]

# now trying to store it in the chroma db 




#preparing vector store for this / colllection meaning table name 
vector_store = Chroma(
    embedding_function=embed_model,
    persist_directory='chroma_db',
    collection_name="sample"
)

#add document mean /data

# vector_store.add_documents(docs) # it takes the list of the document objects 
 


# if we wanted to get the embedding data , document data and the metadatabas then 


# result = vector_store.get(include= ['embeddings','documents','metadatas'])
# print(result)
"""
{'ids': ['7e1a80fd-2490-4c74-acf7-b72b44435894', 'b1219ac1-d510-4ef1-8447-acc63dcd892e', '35e47e9d-e225-412c-b17a-0dabccd10c55', '2ceb69d8-7dd3-4db0-9328-2e4bdb3c3e8f', '200c3eab-10cd-45a4-94ed-3d5caa5ca6d7'], 'embeddings': array([[ 0.00997217,  0.06902205, -0.05149385, ..., -0.0354182 ,
         0.01286431,  0.01236015],
       [ 0.00128301,  0.03122922, -0.02369012, ..., -0.00526653,
        -0.0326956 ,  0.02735758],
       [-0.10275364,  0.02631757,  0.0228163 , ..., -0.0336118 ,
        -0.07977163, -0.01517115],
       [ 0.02125674, -0.02472139, -0.04485311, ..., -0.1099406 ,
         0.00574407,  0.09909566],
       [ 0.01874619,  0.04363557, -0.0429798 , ..., -0.07810399,
        -0.07842913, -0.00308673]], shape=(5, 384)), 'documents': ['Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.', "Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.", 'MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.', 'Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.', 'Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.'], 'uris': None, 'included': ['embeddings', 'documents', 'metadatas'], 'data': None, 'metadatas': [{'team': 'Royal Challengers Bangalore'}, {'team': 'Mumbai Indians'}, {'team': 'Chennai Super Kings'}, {'team': 'Mumbai Indians'}, {'team': 'Chennai Super Kings'}]}
"""

#now if we wanted to query the data based on semantic what we can do is perform the semantic search like below 

updated_result = vector_store.similarity_search(
    query="who is the bowler among these ? ",
    k = 2 
    # how many simimliar objects you wanted to show in results  like below it returned two jadeja and bumrah
) # It returns document object like 
#[Document(id='2ceb69d8-7dd3-4db0-9328-2e4bdb3c3e8f', metadata={'team': 'Mumbai Indians'}, page_content='Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.'),
#  Document(id='b1219ac1-d510-4ef1-8447-acc63dcd892e', metadata={'team': 'Mumbai Indians'}, page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.")]



print(updated_result)

# if we wanted to filter data based on metadata 
#then meta-data filtering 

result  = vector_store.similarity_search_with_score(

    query="",
    filter={"team": "Chennai Super Kings"}
)


print(result)

#[(Document(id='35e47e9d-e225-412c-b17a-0dabccd10c55', metadata={'team': 'Chennai Super Kings'}, page_content='MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.'), 1.8434257507324219)
# , (Document(id='200c3eab-10cd-45a4-94ed-3d5caa5ca6d7', metadata={'team': 'Chennai Super Kings'}, page_content='Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.'), 1.8912675380706787)]


# update documents
updated_doc1 = Document(
    page_content="Virat Kohli, the former captain of Royal Challengers Bangalore (RCB), is renowned for his aggressive leadership and consistent batting performances. He holds the record for the most runs in IPL history, including multiple centuries in a single season. Despite RCB not winning an IPL title under his captaincy, Kohli's passion and fitness set a benchmark for the league. His ability to chase targets and anchor innings has made him one of the most dependable players in T20 cricket.",
    metadata={"team": "Royal Challengers Bangalore"}
)

vector_store.update_document(document_id='7e1a80fd-2490-4c74-acf7-b72b44435894', document=updated_doc1) ##can be seen in sqlite viewer  i have used the embedding_id here 

# if we wanted to delete some record then 

# delete document
vector_store.delete(ids=['7e1a80fd-2490-4c74-acf7-b72b44435894']) #can be seen in sqlite viewer 