from langchain_ollama import ChatOllama 
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate

# -----------------------
# TOOL
# -----------------------

@tool 
def multiply(a: int, b: int) -> int: 
    """given two numbers a and b this tool returns their product"""
    return a * b


# -----------------------
# LLM
# -----------------------

llm = ChatOllama(model="qwen2.5:3b-instruct-q4_K_M")

# Simple system prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant"),
    ("human", "{input}")
])

# Create tool-calling agent
agent = create_tool_calling_agent(llm, [multiply], prompt)

# Agent executor (this is the middleware)
agent_executor = AgentExecutor(agent=agent, tools=[multiply], verbose=True)

# -----------------------
# QUERY
# -----------------------

result = agent_executor.invoke({
    "input": "can you multiply 3 with 10?"
})

print(result["output"])