from langchain_core.tools import StructuredTool
from pydantic import BaseModel , Field


class MultiplyInput(BaseModel):
    a:int = Field(required=True , description="First integer value")
    b:int = Field(required=True , description="Second integer value")


def multiply(a:int,b:int)->int:
    """
    a method for returning the multiplied values
    
    :param a: first integer value
    :type a: int
    :param b: second integer value
    :type b: int
    :return: returns the product 
    :rtype: int
    """
    return a*b 

multiply_tool = StructuredTool(
        func=multiply,
        name = "multiply",
        description= "muiltiply two numbers", 
        args_schema=MultiplyInput
    )

result  = multiply_tool.invoke({"a":6,"b":5})

print(result)
print(multiply_tool.name) #multiply
print(multiply_tool.description) # muiltiply two numbers
print(multiply_tool.args) #{'a': {'description': 'First integer value', 'title': 'A', 'type': 'integer'}, 'b': {'description': 'Second integer value', 'title': 'B', 'type': 'integer'}}
print(multiply_tool.args_schema) #<class '__main__.MultiplyInput'>