# Retrieval Augmented Generation based Q&A System

LLMs when asked highly specific subject matter based questions tend to be vague and hallucinate due to the excess of training corpus they are fed.
This project displays RAGs ability to help improve an LLMs answering capabilities on such queries by providing them with most relevant chunks from required documents,

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

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <repository-name>
```

---

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

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

---

## Running the Project

### Step 1 — Add Documents

Place all PDF files inside:

```text
research/
```

---

### Step 2 — Start FastAPI Backend

```bash
uvicorn rag_chain:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

### Step 3 — Start Streamlit Frontend

```bash
streamlit run app.py
```
