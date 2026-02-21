"""runnable parallel is a runnable primitive that allows multiple runnables
to execute in parallel each runnable receives the same input and processes
independenty producing a dictionary of outputs
both have same input but diffent outputes and they are independent 
"""

from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_classic.schema.runnable import RunnableParallel,RunnableSequence

model = ChatOllama(model="qwen2.5:3b-instruct-q4_K_M")
prompt_1 = PromptTemplate(template="generate a tweet about {topic}", input_variables=['topic'])
prompt_2 = PromptTemplate(template="generate a linkedin post about {topic}",input_variables=['topic'])

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet':RunnableSequence(prompt_1,model,parser),
    'linkedin':RunnableSequence(prompt_2,model,parser)
})


result = parallel_chain.invoke ({"topic":"today i worked on Artificial intelligence"})
print(result)\



# {'tweet': '"Today, I had the privilege of working on advancing arti "Sure! Here's a concise and professional LinkedIn post you can share to highlight your work in artificial intelligence (AI):\n\n---\n\n**Excited to Share My Work in AI Today!**\n\nToday, I focused on advancing our team’s projects by leveraging the latest advancements in AI. From optimizing algorithms for better data processing to creating more intuitive user interfaces, every task involves pushing the boundaries of what's possible with AI.\n\nIt's truly rewarding seeing how AI can transform industries and improve people's lives. What are some ways you're currently exploring or using AI in your work? 💡\n\n---\n\nFeel free to adjust any part to better fit your personal story or industry context!"}












