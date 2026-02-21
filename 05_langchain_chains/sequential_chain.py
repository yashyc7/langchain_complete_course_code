from langchain_core.output_parsers import StrOutputParser 
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate


chat_model = ChatOllama(model="qwen2.5-coder:7b-instruct-q4_K_M")

prompt1 = PromptTemplate(
    template="Genreate a detaild report on {topic}"
    ,input_variables=['topic']

)

prompt2 = PromptTemplate(template="generate a 5 pointer summary from the following text \n {text}",input_variables=['text'])


parser = StrOutputParser()

chain = prompt1 | chat_model | prompt2 | chat_model | parser


result = chain.invoke("black_hole")

print(result)


# 1. **Overview**: Black holes are regions in space with immense gravitational pull that traps everything within their event horizons, including light.

# 2. **Formation**: Stellar black holes form from the collapse of massive stars (5-100 solar masses), while supermassive black holes at galaxy centers can have millions to billions of solar masses.

# 3. **Characteristics**: Key features include an event horizon, singularity, and spacetime curvature.

# 4. **Properties**: They have massive event horizons, extreme gravity, and the possibility of Hawking radiation.

# 5. **Observations**: Indirect evidence like accretion disks, gravitational lensing, X-rays, and gamma rays help infer their existence and properties.
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