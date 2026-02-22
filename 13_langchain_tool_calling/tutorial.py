from langchain_ollama import ChatOllama 
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage

# -----------------------
# TOOL DEFINITION
# -----------------------

@tool 
def multiply(a: int, b: int) -> int: 
    """given two numbers a and b this tool returns their product"""
    return a * b

# -----------------------
# LLM SETUP
# -----------------------

llm = ChatOllama(model="qwen2.5:3b-instruct-q4_K_M")
llm_with_tools = llm.bind_tools([multiply])

# -----------------------
# USER QUERY
# -----------------------

query = HumanMessage(content="can you multiply 3 with 10?")
messages = [query]

# -----------------------
# STEP 1: LLM DECIDES WHETHER TO CALL TOOL
# -----------------------

response = llm_with_tools.invoke(messages)

# -----------------------
# STEP 2: CHECK FOR TOOL CALL
# -----------------------

if response.tool_calls:
    tool_call = response.tool_calls[0]
    
    tool_name = tool_call["name"]
    tool_args = tool_call["args"]
    tool_call_id = tool_call["id"]
    
    # Execute the tool
    if tool_name == "multiply":
        tool_result = multiply.invoke(tool_args)
    
    # -----------------------
    # STEP 3: SEND TOOL RESULT BACK TO LLM
    # -----------------------
    
    tool_message = ToolMessage(
        content=str(tool_result),
        tool_call_id=tool_call_id
    )
    
    messages.append(response)
    messages.append(tool_message)
    
    final_response = llm_with_tools.invoke(messages)
    
    print(final_response.content)

else:
    # If no tool call, print normal LLM response
    print(response.content)