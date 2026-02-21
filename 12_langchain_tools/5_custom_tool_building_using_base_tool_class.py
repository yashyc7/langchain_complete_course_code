from langchain_core.tools import BaseTool
from pydantic import BaseModel , Field
from typing import Type

class MultiplyInput(BaseModel):
    a:int = Field(required=True , description="First integer value")
    b:int = Field(required=True , description="Second integer value")

class MultiplyTool(BaseTool):
    name : str = "multiply"
    description : str =  " multiply two numbers"

    args_schema :Type[BaseModel] = MultiplyInput

    def _run(self, a:int , b: int )->int :
        return a*b 
    
multiply_tool = MultiplyTool()
result = multiply_tool.invoke({"a":10, "b":5})
print(result) # 50
print(multiply_tool.name)  # multiply
print(multiply_tool.description) # multiply two numbers
print(multiply_tool.args) # {'a': {'description': 'First integer value', 'title': 'A', 'type': 'integer'}, 'b': {'description': 'Second integer value', 'title': 'B', 'type': 'integer'}}
print(multiply_tool.args_schema) #  <class '__main__.MultiplyInput'>