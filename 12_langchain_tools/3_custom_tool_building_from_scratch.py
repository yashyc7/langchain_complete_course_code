from langchain_core.tools import tool 

# step1 create a funcion


def multiply(a,b):
    return a*b

#step 2 add type hints 
def  multiply_typehints_added (a:int,b:int)->int:
    """
    returns the multiply of two integer values 
    
    :param a: int
    :param b: int
    """
    return a*b 

#step 3 add the tool decorator 

@tool
def final_multiplication_function(a:int,b:int)->int:
    """
    Docstring for final_multiplication_function
    
    :param a: first integer 
    :type a: int
    :param b: second integer
    :type b: int
    :return: multiplication of two given parameters  
    :rtype: int
    """
    return a*b 


result = final_multiplication_function.invoke({"a":3,"b":6})
print(result ) #18 

print(final_multiplication_function.name) #final_multiplication_function
print(final_multiplication_function.description)
# :param a: first integer
# :type a: int
# :param b: second integer
# :type b: int
# :return: multiplication of two given parameters
# :rtype: int

print(final_multiplication_function.args) #{'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}

