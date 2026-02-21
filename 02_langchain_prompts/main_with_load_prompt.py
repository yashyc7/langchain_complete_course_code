import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import load_prompt

# ---------- Page config ----------
st.set_page_config(
    page_title="Research Paper Summarizer", page_icon="📄", layout="centered"
)


# ---------- Model loader ----------
@st.cache_resource
def load_model():
    return ChatOllama(model="qwen2.5-coder:7b")


# ---------- Header ----------
st.markdown(
    """
    <h1 style="text-align:center;">📄 Research Paper Summarizer</h1>
    <p style="text-align:center; color:gray;">
        Generate structured, style-aware summaries of popular ML papers
    </p>
    """,
    unsafe_allow_html=True,
)

# ---------- Load model ----------
with st.spinner("Loading language model..."):
    chat_model = load_model()

# ---------- Input section ----------
st.markdown("### 🔧 Configuration")

with st.container():
    paper_input = st.selectbox(
        "📘 Research Paper",
        [
            "Attention Is All You Need",
            "BERT: Pre-training of Deep Bidirectional Transformers",
            "GPT-3: Language Models are Few-Shot Learners",
            "Diffusion Models Beat GANs on Image Synthesis",
        ],
    )

    col1, col2 = st.columns(2)

    with col1:
        style_input = st.selectbox(
            "🧠 Explanation Style",
            ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"],
        )

    with col2:
        length_input = st.selectbox(
            "📏 Explanation Length",
            [
                "Short (1-2 paragraphs)",
                "Medium (3-5 paragraphs)",
                "Long (detailed explanation)",
            ],
        )

# ---------- Prompt ----------
template = load_prompt("template.json")
prompt = template.invoke(
    {
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input,
    }
)

# ---------- Action ----------
st.markdown("---")

if st.button("✨ Generate Summary", use_container_width=True):
    with st.spinner("Generating summary..."):
        result = chat_model.invoke(prompt)

    st.markdown("### 📝 Summary Output")
    st.markdown(
        f"""
        <div style="
            background-color:#0e1117;
            padding:20px;
            border-radius:10px;
            border:1px solid #2a2a2a;
        ">
        {result.content}
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------- Footer ----------
st.markdown(
    """
    <hr>
    <p style="text-align:center; color:gray; font-size:12px;">
        Powered by LangChain + Ollama + Streamlit
    </p>
    """,
    unsafe_allow_html=True,
)
