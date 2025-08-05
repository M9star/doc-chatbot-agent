from sklearn import pipeline
from .form_agent import collect_user_info
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain_community.llms import HuggingFacePipeline
from langchain.text_splitter import RecursiveCharacterTextSplitter
import torch
import os


def load_documents(directory_path):
    docs = []  
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            loader = TextLoader(os.path.join(directory_path, filename))  
            docs.extend(loader.load())
        elif filename.endswith('.pdf'):
            from langchain_community.document_loaders import PyPDFLoader
            loader = PyPDFLoader(os.path.join(directory_path, filename))
            docs.extend(loader.load())
    return docs

def create_vector_store(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    splits = text_splitter.split_documents(docs)
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(splits, embeddings)
    return vectordb


def build_qa_chain(vectordb):
    from transformers import pipeline
    hf_pipeline = pipeline("text2text-generation", model="google/flan-t5-base", device=0 if torch.cuda.is_available() else -1)
    llm = HuggingFacePipeline(pipeline=hf_pipeline)
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm,
        vectordb.as_retriever()
    )
    return qa_chain, llm



if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    docs = load_documents(data_dir)
    vectordb = create_vector_store(docs)
    qa_chain = build_qa_chain(vectordb)
    
    chat_history = []
    print("Ask your question (type 'exit' to quit):")
    while True:
        query = input(">> ").strip()
        if query.lower() == 'exit':
            break
        # Check for appointment or call intent
        if any(kw in query.lower() for kw in ["book appointment", "call me", "schedule meeting", "contact me"]):
            user_info = collect_user_info()
            print("Collected user info:", user_info)
            # Save to file
            with open("appointments.txt", "a") as f:
                f.write(f"{user_info['name']}, {user_info['phone']}, {user_info['email']}, {user_info['date']}\n")
            print("Your appointment has been saved.")
            continue
        result = qa_chain({"question": query, "chat_history": chat_history})
        print("Answer:", result['answer'])
        chat_history.append((query, result['answer']))



