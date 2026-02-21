"""Runnable lambda is a runnable primitive that allows you to apply custom 
python functions with an ai pipeline..add()


it acts as an middleware between diffent ai components. 
enabling preprocesing transformation api cals filterin and post processing in a
langchain workflow 

"""

# in simplewords we can convert any function in python 
# to a runnable 

# suppose i wanted to print the topic content and number of words like calculation thing right 

#LLM's suck at calculation we must not give llm's to go calculation 
# for saving context and processing power 


from langchain_ollama import ChatOllama
from langchain_classic.schema.runnable import RunnablePassthrough, RunnableSequence,RunnableParallel,RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 

def word_count(text):
    return len (text.split()) # convert to list and then return length or count



parser = StrOutputParser ()


# if we wanetd to pring joke and explaination both when we wanted to modify results in between understood 


model = ChatOllama(model="qwen2.5:3b-instruct-q4_K_M")




prompt_1 = PromptTemplate(template="write a joke about topic {topic}",input_variables=['topic'])
prompt_2= PromptTemplate(template= "explain the following joke {text}",input_variables=['text'])


joke_gen_chain = RunnableSequence(prompt_1,model,parser)


parallel_chain = RunnableParallel({
    "joke":RunnablePassthrough(),
    "words_lengh":RunnableLambda(word_count)
})

final_chain = RunnableSequence (joke_gen_chain,parallel_chain)

print(final_chain.invoke({"topic":"cricket"}))

print(final_chain.get_graph().print_ascii())

# {'joke': "Sure, here’s a light-hearted cricket-themed joke for you:\n\nWhy don't crickets make good dancers? Because they always end up jumping to the wrong beat!", 'words_lengh': 24}
#               +-------------+
#               | PromptInput |
#               +-------------+
#                       *
#                       *
#                       *
#              +----------------+
#              | PromptTemplate |
#              +----------------+
#                       *
#                       *
#                       *
#                +------------+
#                | ChatOllama |
#                +------------+
#                       *
#                       *
#                       *
#             +-----------------+
#             | StrOutputParser |
#             +-----------------+
#                       *
#                       *
#                       *
#     +---------------------------------+
#     | Parallel<joke,words_lengh>Input |
#     +---------------------------------+
#               **            ***
#             **                 **
#           **                     **
# +-------------+              +------------+
# | Passthrough |              | word_count |
# +-------------+              +------------+
#               **            ***
#                 **        **
#                   **    **
#     +----------------------------------+
#     | Parallel<joke,words_lengh>Output |
#     +----------------------------------+