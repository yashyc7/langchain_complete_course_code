from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.schema.runnable import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()


model = ChatOllama(model="qwen2.5-coder:7b-instruct-q4_K_M")

parser = StrOutputParser()

class Feedback(BaseModel):

    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback': 'This is a beautiful phone'}))

chain.get_graph().print_ascii()


# Thank you for your kind words! It's great to know that my assistance has been appreciated. If you have any more questions or need further help in the future, please don't hesitate to ask. I'm here to assist you with any queries you may have.
#     +-------------+      
#     | PromptInput |
#     +-------------+
#             *
#             *
#             *
#    +----------------+
#    | PromptTemplate |
#    +----------------+
#             *
#             *
#             *
#      +------------+
#      | ChatOllama |
#      +------------+
#             *
#             *
#             *
# +----------------------+
# | PydanticOutputParser |
# +----------------------+
#             *
#             *
#             *
#        +--------+
#        | Branch |
#        +--------+
#             *
#             *
#             *
#     +--------------+
#     | BranchOutput |
#     +--------------+













