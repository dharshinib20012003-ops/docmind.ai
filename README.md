DocuMind - RAG Based Document Question Answering System



Overview

DocuMind is a Retrieval-Augmented Generation (RAG) system that enables users to query information from PDF documents.

Instead of manually reading large documents, users can ask natural language questions and receive relevant answers.



Problem Statement

Organizations deal with large volumes of documents (invoices, reports, manuals).

Manual searching is inefficient.



Solution:

\- Ingest documents

\- Process and index data

\- Retrieve relevant content

\- Answer queries



Architecture (Block Diagram)



User Query

&#x20;  ↓

Query Processing

&#x20;  ↓

FAISS Vector DB (stores embeddings)

&#x20;  ↓

Retrieve Relevant Chunks

&#x20;  ↓

Context + Question

&#x20;  ↓

Local NLP Model

&#x20;  ↓

Final Answer



Implementation Steps



1\. Document Ingestion (PyPDFLoader)

2\. Text Chunking (RecursiveCharacterTextSplitter)

3\. Embeddings (HuggingFaceEmbeddings)

4\. Storage (FAISS)

5\. Retrieval (Similarity Search)

6\. Answer Generation (Transformers model)



Data Flow



PDF → Chunking → Embeddings → FAISS

Query → Embedding → Search → Context → Model → Answer



Tech Stack

Python, LangChain, FAISS, HuggingFace Transformers



Run

python test\_rag.py



Example

Q: What is total amount?

A: 50500 INR

