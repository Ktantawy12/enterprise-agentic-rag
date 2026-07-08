import streamlit as st

from src.rag.chain import ask


st.set_page_config(
    page_title="Enterprise Agentic RAG",
    page_icon="🤖",
)

st.title("🤖 Enterprise Agentic RAG")

st.write(
    "Ask questions about the uploaded banking documents."
)

question = st.text_input(
    "Enter your question:"
)

if st.button("Ask"):

    if question:

        with st.spinner("Thinking..."):

            answer = ask(question)

        st.subheader("Answer")

        st.write(answer)