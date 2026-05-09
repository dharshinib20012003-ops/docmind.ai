# DocuMind AI – RAG-Based Document Question Answering System

## 🚀 Overview

DocuMind AI is an end-to-end **Retrieval-Augmented Generation (RAG)** system that enables users to extract insights from PDF documents using natural language queries.

Instead of manually reading long documents, users can ask questions and receive context-aware answers generated from the document content.

---

## 🎯 Problem Statement

Large documents such as invoices, reports, and manuals are difficult to navigate manually.
Traditional keyword search fails to capture semantic meaning.

**Goal:** Build a system that understands documents and answers user queries intelligently.

---

## 🧠 System Architecture

```
                User Query
                     │
                     ▼
           Query Embedding Generation
                     │
                     ▼
        FAISS Vector Database (Embeddings)
                     │
                     ▼
         Retrieve Relevant Chunks
                     │
                     ▼
     Context + User Query Formation
                     │
                     ▼
        Local Language Model (HF)
                     │
                     ▼
               Final Answer
```

---

## ⚙️ How It Works (Step-by-Step)

### 1. Document Ingestion

* PDFs loaded using `PyPDFLoader`
* Extracts raw text data

### 2. Text Chunking

* Splits large text into smaller chunks
* Uses `RecursiveCharacterTextSplitter`
* Improves retrieval accuracy

### 3. Embedding Generation

* Converts text chunks into vectors
* Uses HuggingFace embeddings
* Enables semantic search

### 4. Vector Storage

* Stores embeddings in FAISS
* Fast similarity search

### 5. Retrieval

* User query converted to embedding
* Top relevant chunks retrieved

### 6. Answer Generation

* Context + query passed to local model
* Generates final response

---

## 🔄 Data Flow

```
PDF → Text Extraction → Chunking → Embeddings → FAISS
                                             ↓
User Query → Embedding → Similarity Search → Context
                                             ↓
                               Model → Answer
```

---

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** LangChain
* **Vector Database:** FAISS
* **Embeddings:** HuggingFace
* **Model:** Transformers (local inference)

---

## 📂 Project Structure

```
docmind.ai/
│
├── app/
│   └── rag_pipeline.py
│
├── data/
│   └── docs/
│
├── test_rag.py
├── interactive_chat.py
├── .gitignore
└── README.md
```

---

## ▶️ How to Run

```bash
git clone https://github.com/dharshinib20012003-ops/docmind.ai
cd docmind.ai

pip install -r requirements.txt
python test_rag.py
```

---

## 💡 Example

**Input:**

```
What is the total amount?
```

**Output:**

```
50500 INR
```

---

## 🚧 Limitations

* Uses lightweight local model → limited reasoning ability
* Works best on structured/simple PDFs
* No UI (CLI-based interaction only)

---

## 🚀 Future Improvements

* Add FastAPI backend for API access
* Build UI using Streamlit/React
* Support multiple document uploads
* Integrate stronger LLMs (Llama / Mistral)
* Improve answer accuracy with better prompting

---

## ⭐ Key Highlights

* Built complete RAG pipeline from scratch
* Implemented semantic search using FAISS
* Integrated document processing with NLP
* Demonstrates real-world data engineering + AI workflow

---

## 📌 Author

Dharshini Arvind Kumar
