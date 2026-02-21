from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate


chat_model = ChatOllama(model="qwen2.5-coder:7b-instruct-q4_K_M")


prompt = PromptTemplate(template="Genereate 5 intresting facts about {topic}"
                       , input_variables=['topic'])

parser = StrOutputParser()


chain = prompt | chat_model | parser 

# | is called pipe operator LECL 
result = chain.invoke({'topic':'car'})

print(result)

# 1. **The First Car Accident**: The first recorded car accident happened in 1896 near Paris, France. A Benz Patent-Motorwagen (a type of early gasoline-powered vehicle) crashed into a horse-drawn carriage. Interestingly, the driver and two passengers were not injured.

# 2. **Most Expensive Car Insurance Policy**: As of my last update in October 2023, the most expensive car insurance policy ever issued was for a Lotus Evora S, which costs around $6 million per year. This level of coverage is typically associated with luxury vehicles and collectors' items.

# 3. **First Electric Car**: The first electric car was invented by Robert Anderson in 1837, using a lead-acid battery. However, the development of the internal combustion engine overshadowed electric vehicles for most of the last century. Only recently has there been a resurgence in interest in electric cars due to environmental concerns.      

# 4. **Most Expensive Car**: The most expensive car ever sold at auction was a 1962 Ferrari 250 GTO Nürburgring, which was auctioned off for $73 million in October 2018. This record-breaking sale reflects the continued fascination with classic and rare vehicles.

# 5. **First Car Model**: The first mass-produced car model was the Ford Model T, introduced by Henry Ford in 1908. This model became incredibly popular due to its affordability and reliability, making it accessible to a wide range of consumers for the first time.


# if we wanted to visualize then 


chain.get_graph().print_ascii()
#      +-------------+       
#      | PromptInput |
#      +-------------+
#             *
#             *
#             *
#     +----------------+
#     | PromptTemplate |
#     +----------------+
#             *
#             *
#             *
#       +------------+
#       | ChatOllama |
#       +------------+
#             *
#             *
#             *
#    +-----------------+
#    | StrOutputParser |
#    +-----------------+
#             *
#             *
#             *
# +-----------------------+
# | StrOutputParserOutput |
# +-----------------------+