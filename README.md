<div align="center">

# Retrieval Augmented Generation based Q&A System

LLMs when asked highly specific subject matter questions often produce vague or hallucinated responses due to the breadth of their training corpus.

This project demonstrates how Retrieval Augmented Generation (RAG) improves answer quality by retrieving the most relevant document chunks and grounding the LLM response in contextual information.

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-121212?style=for-the-badge)
![FAISS](https://img.shields.io/badge/FAISS-0467DF?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)

</div>

---

## Features

- PDF based document ingestion
- Semantic search using dense vector embeddings
- FAISS powered similarity retrieval
- Context grounded answer generation
- LangGraph based retrieval-generation workflow
- Streamlit frontend for interaction
- Modular backend architecture for easy extension

---

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python |
| LLM Orchestration | LangChain |
| Workflow Graph | LangGraph |
| Vector Database | FAISS |
| Embeddings | Hugging Face Embeddings |
| LLM Provider | Hugging Face Inference API |
| PDF Parsing | PyPDFLoader |
| Text Chunking | RecursiveCharacterTextSplitter |
| Frontend | Streamlit |
| Backend API | FastAPI |

---

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <repository-name>
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / MacOS

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```


### 5. Configure Environment Variables

Create a `.env` file in the project root:

```env
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

---

## Running the Project

### 1. Add Documents

Place all PDF files inside:

```text
research/
```

### 2. Start FastAPI Backend

```bash
uvicorn rag_chain:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

### 3. Start Streamlit Frontend

```bash
streamlit run app.py
```

## File Structure

```text
├── app.py                 # Streamlit frontend
├── rag_chain.py           # RAG pipeline and FastAPI backend
├── requirements.txt       # Project dependencies
├── .env                   # Hugging Face API token
├── research/              # PDF document corpus
│   ├── paper1.pdf
│   ├── paper2.pdf
│   └── ...
```

