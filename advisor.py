import os
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.chains import RetrievalQA

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Paths
CATALOG_PATH = "catalog_data/catalog.txt"
VECTORSTORE_DIR = "vector_store"

# Initialize LLM and Embeddings
llm = ChatOpenAI(model="gpt-3.5-turbo")
embeddings = OpenAIEmbeddings()

def build_vectorstore():
    """Builds a FAISS vectorstore from the catalog data."""
    loader = TextLoader(CATALOG_PATH)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    texts = text_splitter.split_documents(docs)
    
    vectorstore = FAISS.from_documents(texts, embeddings)
    vectorstore.save_local(VECTORSTORE_DIR)
    print("✅ Vectorstore built and saved!")

def load_vectorstore():
    """Loads the existing FAISS vectorstore."""
    return FAISS.load_local(VECTORSTORE_DIR, embeddings)

def get_qa_chain():
    """Creates the QA chain using LangChain's RetrievalQA."""
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain

if __name__ == "__main__":
    build_vectorstore()
