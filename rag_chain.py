from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langgraph.graph import START, StateGraph
from typing_extensions import List, TypedDict
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint, ChatHuggingFace
import faiss
import os
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

class State(TypedDict):
    question: str
    context: List[Document]
    answer: str

model = HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.1-8B-Instruct", task='text-generation')
llm = ChatHuggingFace(llm=model)

embeddings = HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')
embedding_dim = len(embeddings.embed_query("hello world"))

index = faiss.IndexFlatL2(embedding_dim)
vector_store = FAISS(
    embedding_function=embeddings,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)

def setup_vector_store(pdf_folder="research"):
    all_docs = []
    for file in os.listdir(pdf_folder):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(pdf_folder, file))
            all_docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = splitter.split_documents(all_docs)
    vector_store.add_documents(splits)

def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["question"], k=3)
    return {"context": retrieved_docs}

def generate(state: State):
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    prompt_input = prompt.format(question=state["question"], context=docs_content)
    response = llm.invoke(prompt_input)
    return {"answer": response.content}

def answer_question(question: str) -> str:
    result = graph.invoke({"question": question})
    return result["answer"]

prompt = PromptTemplate(
    template="""
You are a precise technical assistant. Answer the user question using ONLY the following retrieved context. 

---
CONTEXT:
{context}
---

INSTRUCTIONS:
1. If the answer is not contained within the context, say "I do not have enough information in the research documents to answer this."
2. Do not use outside knowledge.
3. Keep the response professional and concise.

QUESTION: 
{question}

ANSWER:
""".strip(), 

    input_variables=["question", "context"]
)


graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()

setup_vector_store()

app = FastAPI()

@app.post("/chat")
def chat(query : dict):
    question = query['question']
    response = answer_question(question)
    return {'answer' : response}


