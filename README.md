<h1 align="center">
  Retrieval Augmented Generation based Q&A System
</h1>

<br>

<p align="center">

  <img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=python&logoColor=white">

  <img src="https://img.shields.io/badge/LangChain-121212.svg?style=for-the-badge">

  <img src="https://img.shields.io/badge/FAISS-0467DF.svg?style=for-the-badge">

  <img src="https://img.shields.io/badge/FastAPI-009688.svg?style=for-the-badge&logo=fastapi&logoColor=white">

  <img src="https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white">

  <img src="https://img.shields.io/badge/HuggingFace-FFD21E.svg?style=for-the-badge&logo=huggingface&logoColor=black">

</p>

##

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

