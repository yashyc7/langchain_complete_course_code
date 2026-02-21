from langchain_core.output_parsers import JsonOutputParser
from langchain_ollama import ChatOllama 
from langchain_core.prompts import PromptTemplate 


chat_model = ChatOllama(model="qwen2.5:3b-instruct-q4_K_M")
parser = JsonOutputParser()

template = PromptTemplate(template="give me the name, age  and and city of the fictional person \n {format_instructions} ",
                          input_variables=[],
                          partial_variables={"format_instructions":parser.get_format_instructions()}                          
                          )

prompt = template.format ()

result = chat_model.invoke(prompt)

#result is arbiratory like mix of str and json so we have to parse it to json using this parser 


final_result = parser.parse(result.content)

print(final_result)
# {'name': 'Evelyn Harper', 'age': 35, 'city': 'New York'}
# <class 'dict'>

print(type(final_result)) # class dict because python treats json obj as dict 



