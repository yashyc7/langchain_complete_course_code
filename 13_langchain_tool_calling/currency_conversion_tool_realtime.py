from langchain_core.tools import tool
import os
from dotenv import load_dotenv
import requests
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_ollama import ChatOllama

load_dotenv()
API_KEY = os.getenv("API_KEY")

# ---------------------------
# Tool 1: Get conversion rate
# ---------------------------

@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """Fetch currency conversion factor between base and target currency."""
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    data = response.json()

    if data.get("result") != "success":
        raise Exception(f"API error: {data}")

    return data["conversion_rate"]


# ---------------------------
# Tool 2: Convert amount
# ---------------------------

@tool
def convert(amount: float, rate: float) -> float:
    """Convert amount using exchange rate."""
    return amount * rate


# ---------------------------
# LLM Setup
# ---------------------------

llm = ChatOllama(model="qwen2.5:3b-instruct-q4_K_M")
llm_with_tools = llm.bind_tools([get_conversion_factor, convert])

messages = [HumanMessage(content="can you get the conversion rate and convert  10 USD to INR")]

# ---------------------------
# First model call
# ---------------------------

ai_message = llm_with_tools.invoke(messages)
messages.append(ai_message)

conversion_rate = None

# ---------------------------
# Execute tool calls manually
# ---------------------------

for tool_call in ai_message.tool_calls:

    if tool_call["name"] == "get_conversion_factor":
        tool_result = get_conversion_factor.invoke(tool_call["args"])
        conversion_rate = tool_result

        messages.append(
            ToolMessage(
                content=str(tool_result),
                tool_call_id=tool_call["id"],
            )
        )

    elif tool_call["name"] == "convert":
        if conversion_rate is None:
            raise Exception("Conversion rate not available before convert call")

        tool_call["args"]["rate"] = conversion_rate

        tool_result = convert.invoke(tool_call["args"])

        messages.append(
            ToolMessage(
                content=str(tool_result),
                tool_call_id=tool_call["id"],
            )
        )

# ---------------------------
# Final model call
# ---------------------------

final_response = llm_with_tools.invoke(messages)
print(final_response.content)