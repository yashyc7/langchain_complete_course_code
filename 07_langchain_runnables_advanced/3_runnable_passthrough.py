"""
Docstring for 3_runnable_passthrough

runnable passthrough is a special primitive that simply returns the input as 
output without modifying it ? 

"""

from langchain_ollama import ChatOllama
from langchain_classic.schema.runnable import RunnablePassthrough, RunnableSequence,RunnableParallel
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 

parser = StrOutputParser ()


# if we wanetd to pring joke and explaination both when we wanted to modify results in between understood 


model = ChatOllama(model="qwen2.5:3b-instruct-q4_K_M")




prompt_1 = PromptTemplate(template="write a joke about topic {topic}",input_variables=['topic'])
prompt_2= PromptTemplate(template= "explain the following joke {text}",input_variables=['text'])


joke_gen_chain = RunnableSequence(prompt_1,model,parser)


parallel_chain = RunnableParallel({
    "joke":RunnablePassthrough(),
    "explaination":RunnableSequence(prompt_2,model,parser)
})

final_chain = RunnableSequence (joke_gen_chain,parallel_chain)

print(final_chain.invoke({"topic":"cricket"}))

print(final_chain.get_graph().print_ascii())

# {'joke': "Sure! Here's a light-hearted cricket-themed joke for you:\n\nWhy don't crickets make good dancers? Because they have two left feet! (Although technically they only have one right foot, it’s funnier this way!)", 'explaination': 'You\'re absolutely correct with your playful twist on the joke. Crickets are indeed known for their chirping sound, which many associate with nighttime and summer in certain cultures. Your adaptation of a classic "two left feet" dance joke is clever and fits well with cricket humor. Here it is again:\n\nWhy don\'t crickets make good dancers? Because they have two left feet!\n\nThis version adds a fun twist that plays on both the cricket\'s name and the traditional joke structure, making it even more entertaining.'}
#                   +-------------+
#                   | PromptInput |
#                   +-------------+
#                           *
#                           *
#                           *
#                 +----------------+
#                 | PromptTemplate |
#                 +----------------+
#                           *
#                           *
#                           *
#                   +------------+
#                   | ChatOllama |
#                   +------------+
#                           *
#                           *
#                           *
#                 +-----------------+
#                 | StrOutputParser |
#                 +-----------------+
#                           *
#                           *
#                           *
#         +----------------------------------+
#         | Parallel<joke,explaination>Input |
#         +----------------------------------+
#                  **              ***
#               ***                   **
#             **                        ***
# +----------------+                       **
# | PromptTemplate |                        *
# +----------------+                        *
#           *                               *
#           *                               *
#           *                               *
#   +------------+                          *
#   | ChatOllama |                          *
#   +------------+                          *
#           *                               *
#           *                               *
#           *                               *
# +-----------------+               +-------------+
# | StrOutputParser |               | Passthrough |
# +-----------------+               +-------------+
#                  **              **
#                    ***        ***
#                       **    **
#        +-----------------------------------+
#        | Parallel<joke,explaination>Output |
#        +-----------------------------------+
# None