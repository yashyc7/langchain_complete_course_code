#runnable sequence is a sequential chain of runnables in langchin that executes each step  one after another , passing the 
# output of one step as the input to the next . 
#it is useful when you need to compose multiple runnables together in a structured view. 
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_classic.schema.runnable import RunnableSequence
from langchain_core.prompts import PromptTemplate


prompt = PromptTemplate(template="write a joke about topic {topic}",input_variables=['topic'])
prompt_2= PromptTemplate(template= "explain the following joke {text}",input_variables=['text'])

model = ChatOllama (model = "qwen2.5:3b-instruct-q4_K_M")

parser = StrOutputParser()

chain = RunnableSequence(prompt,model,parser,prompt_2,model,parser)

result = chain.invoke({"topic":"car"})

print(result)


#if we dont want all output at once like we wanted stream data one by one word then
# from langchain_core.output_parsers import StrOutputParser
# from langchain_ollama import ChatOllama
# from langchain_classic.schema.runnable import RunnableSequence
# from langchain_core.prompts import PromptTemplate

# prompt = PromptTemplate(
#     template="write a joke about topic {topic}",
#     input_variables=["topic"]
# )

# prompt_2 = PromptTemplate(
#     template="explain the following joke {text}",
#     input_variables=["text"]
# )

# model = ChatOllama(model="qwen2.5:3b-instruct-q4_K_M")
# parser = StrOutputParser()

# chain = RunnableSequence(prompt, model, parser, prompt_2, model, parser)

# for chunk in chain.stream({"topic": "car"}):
#     print(chunk, end="", flush=True)
