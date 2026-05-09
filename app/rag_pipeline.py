from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline


def load_and_process(pdf_path):

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings()

    db = FAISS.from_documents(docs, embeddings)

    return db



# ✅ LOAD QA MODEL ONCE
qa_pipeline = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad"
)


def ask_question(db, query):
    docs = db.similarity_search(query)
    context = "\n".join([doc.page_content for doc in docs])
    result = qa_pipeline(
        question=query,
        context=context
    )
    return result["answer"]
