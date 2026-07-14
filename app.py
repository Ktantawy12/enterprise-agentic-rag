import streamlit as st

from src.graph.graph import graph
from src.vectordb.chroma_db import load_vector_store


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="📚",
    layout="wide",
)

load_vector_store()


# --------------------------------------------------
# Session State
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title("📚 AI Research Assistant")

    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")

    st.subheader("Capabilities")

    st.markdown(
        """
- 📄 Answer questions from uploaded documents
- 🔍 Search academic papers
- 🌟 Discover seminal papers
- 🤝 Find related research
- 🕸️ Explore citation networks
"""
    )

    st.markdown("---")

    st.subheader("Example Questions")

    st.markdown(
        """
### 📄 Document Questions

- What documents are required for a personal loan?
- What is the maximum loan amount?
- What is the interest rate?

### 🔬 Research Questions

- Find papers about LangGraph
- Find seminal papers about transformers
- Find papers about SQL

### 📑 Paper Commands

- DOI:10.48550/arXiv.1706.03762
- recommend:https://openalex.org/W4405094415
- network:https://openalex.org/W4405094415
"""
    )

    st.markdown("---")

    st.caption("Version 1.0")


# --------------------------------------------------
# Main Page
# --------------------------------------------------

st.title("📚 AI Research Assistant")

st.caption(
    "Ask questions about your uploaded documents or explore academic research using OpenAlex."
)


# --------------------------------------------------
# Display Chat History
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# --------------------------------------------------
# Chat Input
# --------------------------------------------------

question = st.chat_input("Ask a question...")


if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.spinner("Thinking..."):

        try:

            state = {
                "question": question,
                "route": "",
                "answer": "",
                "documents": [],
            }

            result = graph.invoke(state)

            answer = result["answer"]

        except Exception as e:

            answer = f"❌ {e}"

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)