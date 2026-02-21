from langchain_classic.output_parsers import StructuredOutputParser,ResponseSchema

from langchain_ollama import ChatOllama 
from langchain_core.prompts import PromptTemplate 


chat_model = ChatOllama(model="qwen2.5:3b-instruct-q4_K_M")

schema = [

    ResponseSchema(name = 'field1',description="fact 1  about the topic  "),
    ResponseSchema(name = 'field2',description="fact 2  about the topic  "),
    ResponseSchema(name = 'field3',description="fact 3  about the topic  ")

]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(template="tell me about {topic} \n {format_instructions} ",
                          input_variables=["topic"],
                          partial_variables={"format_instructions":parser.get_format_instructions()}                          
                          )

prompt = template.invoke ({"topic":"black hole"})

result = chat_model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)

print(type(final_result)) 


