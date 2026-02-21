from langchain_ollama import ChatOllama
from typing import TypedDict, Annotated, Literal, Optional


chat_model = ChatOllama(model="qwen2.5:3b-instruct-q4_K_M")


# creating schema for strucuted outupt


class Review(
    TypedDict
):  # WE DONT HAVE VALIDATIONS IN TYPED DICT FOR OUTPUT SO THAT WE USE PYDANTIC
    key_themes: Annotated[
        list[str], "Write down all the key themes discussed in the review in a list"
    ]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[
        Literal["pos", "neg"],
        "Return sentiment of the review either negative, positive or neutral",
    ]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]


structured_output_chat_model = chat_model.with_structured_output(Review)

result = structured_output_chat_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh""")

print(result)

# {'summary': "Nitish Singh's review of the Samsung Galaxy S24 Ultra highlights its powerful features, particularly in terms of processing speed, camera quality, and battery life. He praises the Snapdragon 8 Gen 3 processor for handling heavy tasks efficiently, the impressive 200MP night mode with excellent zoom capabilities, and the robust battery performance lasting a full day even under high usage conditions. However, he also points out some drawbacks such as a heavier weight and size making it uncomfortable for one-handed use, bloatware within One UI, and its steep price tag of $1,300.", 'sentiment': 'positive', 'rating': 4}


# now the output datatype will be <class dict>
