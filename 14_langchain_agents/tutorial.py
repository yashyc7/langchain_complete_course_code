from langchain_ollama import ChatOllama
from langchain_core.tools import tool 
from langchain.agents import create_agent
from langchain.messages import AIMessage
from dotenv import load_dotenv
import requests 
from langgraph.checkpoint.memory import InMemorySaver
import os 
from datetime import datetime  

load_dotenv()

API_KEY = os.getenv("API_KEY")

@tool
def multiply(a: int, b: int) -> int:
    """Return the product of two numbers."""
    return a * b

@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """Fetch currency conversion factor between base and target currency."""
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    data = response.json()
    if data.get("result") != "success":
        raise Exception(f"API error: {data}")
    return data["conversion_rate"]

@tool
def get_current_date() -> str:
    """Return the current date."""
    return datetime.now().strftime("%Y-%m-%d")


# ✅ Use a larger model that supports tool calling
llm = ChatOllama(model="qwen2.5:3b-instruct-q4_K_M", temperature=0)

tools = [get_current_date,get_conversion_factor,multiply]
memory = InMemorySaver()

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a helpful assistant. Use tools to answer questions.",
    checkpointer=memory
)

query = "your first task is to get the todays date and second task is to convert 10 usd to inr and  after conversion multiply the converted answer with 3  "

config = {"configurable": {"thread_id": "user_123"}}
# ✅ Correct input format + stream_mode="values"
for chunk in agent.stream(
    {"messages": [{"role": "user", "content": query}]},
    stream_mode="values",
    config=config
):
    latest = chunk["messages"][-1]

    if isinstance(latest, AIMessage):
        if latest.content:
            print(f"\nAgent: {latest.content}")
        elif latest.tool_calls:
            for tc in latest.tool_calls:
                print(f"\n> Calling tool: `{tc['name']}` with input: `{tc['args']}`")
    else:
        # ToolMessage (tool result)
        print(f"\n> Tool result: {latest.content}")
    
    print("---")