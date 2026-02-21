from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import streamlit as st
import os

os.environ['HF_HOME'] = 'D:/Huggingface_cache'

@st.cache_resource
def load_model():
    llm = HuggingFacePipeline.from_model_id(
        model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        task="text-generation",
        pipeline_kwargs={
            "temperature": 0.5,
            "max_new_tokens": 100
        },
    )
    return ChatHuggingFace(llm=llm)

chat_model = load_model()

st.header("Summarizer Tool")

user_input = st.text_input("Enter your prompt")

if st.button("Summarize"):
    if user_input.strip():
        with st.spinner("Generating response..."):
            result = chat_model.invoke(user_input)
            st.write(result.content)
    else:
        st.warning("Please enter a prompt.")
