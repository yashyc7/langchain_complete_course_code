from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from langchain_ollama import ChatOllama 
from langchain_core.prompts import PromptTemplate 


chat_model = ChatOllama(model="qwen2.5:3b-instruct-q4_K_M")


class Person (BaseModel):
    name : str = Field(description= " name of the person ")
    age : int = Field (description= " the age of the person in integer ")
    city : str = Field (description= " city to which person belongs to")
    additional_information : dict = Field (description= "additional information about that person")

parser = PydanticOutputParser(pydantic_object=Person)


template = PromptTemplate(template="Give me the details about random person from {country} \n {format_instructions} ",
                          input_variables=["country"],
                          partial_variables={"format_instructions":parser.get_format_instructions()}                          
                          )

prompt = template.invoke ({"country":"india"})

result = chat_model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)

print(type(final_result)) 


