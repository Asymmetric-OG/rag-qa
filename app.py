import streamlit as st
import requests

st.set_page_config(page_title="RAG Q&A Powered by FastAPI", layout="centered")
st.title("Ask a Query")
st.write("Ask a question based on the uploaded documents")

question = st.text_input("Enter your question:")

API_ENDPOINT='http://127.0.0.1:8000/chat'


if st.button("Ask"):
    query = {'question' : question}
    if not query['question'].strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            response = requests.post(url=API_ENDPOINT, json=query)
            st.write(response.json()['answer'])
