import os
import streamlit as st # the UI
from langchain_groq import ChatGroq # for creating the chatbot
from langchain.text_splitter import RecursiveCharacterTextSplitter # to split the doc into small sizes/chunks
from langchain.chains.combine_documents import create_stuff_documents_chain #  
from langchain_core.prompts import ChatPromptTemplate # creating prompt template
from langchain.chains import create_retrieval_chain
from langchain.vectorstores.faiss import FAISS # embedding the vector store database
from langchain_community.document_loaders import PyPDFDirectoryLoader # to load the pdf
from langchain_google_genai import GoogleGenerativeAIEmbeddings # to embed the vector
import time

from dotenv import load_dotenv

load_dotenv()

##Load the Groq and Google api keys from .env

groq_api_key = os.getenv("GROQ_API_KEY")
os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")


st.title("Pemi's Document Q&A")
st.subheader("Hello!, Welcome to my Q&A Application")
#st.write("PS: You can ask questions base on the contents of the document provided.")

llm = ChatGroq(groq_api_key = groq_api_key, model_name = "Gemma-7b-It")

prompt = ChatPromptTemplate.from_template(
"""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question
<context>
{context}
<context>
Questions:{input}

"""
)

def vector_embedding():
    if "vectors" not in st.session_state:
        with st.spinner("Creating vector store, please wait..."):
            st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
            st.session_state.loader = PyPDFDirectoryLoader("./Questions") # data ingestion
            st.session_state.docs = st.session_state.loader.load() #docs load
            st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs)
            st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)
        st.success("Vector store DB is ready")

# Interface for creating the vector store
st.header("Setup Vector Store")
st.write("Click the button to create the vector store from the document.")
if st.button("Create Vector Store"):
    vector_embedding()

# Interface for entering the question
st.header('Ask a Question')
st.write("click the button below")
with st.form(key='question_form'):
    prompt1 = st.text_input("Enter your Question from the document")
    submit_button = st.form_submit_button(label='Submit Question')

if submit_button and prompt1:
    try:
        document_chain = create_stuff_documents_chain(llm, prompt)
        retriever = st.session_state.vectors.as_retriever()
        retrieval_chain = create_retrieval_chain(retriever, document_chain)


        with st.spinner("Generating response, please wait..."):
            start = time.process_time()
            response = retrieval_chain.invoke({'input': prompt1})
            response_time = time.process_time() - start
    
        st.write("Response time: {:.2f} seconds".format(response_time))
        st.write(response['answer'])

        with st.expander("Document Similarity Search"):
            for i, doc in enumerate(response["context"]):
                st.write(doc.page_content)
                st.write("............")
    except Exception as e:
        st.error(f"An error occurred: {e}")
