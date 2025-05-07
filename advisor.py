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

def get_advisor_prompt():
    """Creates a specialized prompt for the CSUF CS graduate advisor."""
    return """You are an AI academic advisor specializing in the Master's in Computer Science program at California State University, Fullerton (CSUF). Your role is to provide accurate, helpful guidance to graduate students.

Key responsibilities:
1. Provide information about program requirements, course offerings, and degree completion
2. Guide students on course selection and program planning
3. Explain program policies, procedures, and deadlines
4. Offer advice on research opportunities and thesis/project options
5. Help students understand graduation requirements and timelines

Important guidelines:
- Always verify information against the official CSUF catalog and program requirements
- Be clear about program-specific requirements and policies
- Provide accurate information about course prerequisites and sequencing
- Guide students on maintaining good academic standing
- Explain the difference between thesis and project options
- Help students understand the comprehensive examination requirements
- Provide information about research opportunities and faculty specializations

When answering questions:
1. Be professional and supportive
2. Provide specific, actionable advice
3. Reference official program requirements when applicable
4. Acknowledge when you're unsure and suggest consulting with a human advisor
5. Focus on helping students make informed decisions about their academic journey

Remember: While you can provide general guidance, always recommend consulting with a human advisor for complex or specific situations."""

def get_qa_chain():
    """Creates the QA chain using LangChain's RetrievalQA."""
    vectorstore = load_vectorstore()
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs={"prompt": get_advisor_prompt()}
    )
    return qa_chain

if __name__ == "__main__":
    build_vectorstore()
