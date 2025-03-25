![image](https://github.com/user-attachments/assets/28c1c48c-3d06-464e-84a7-7ef3f8576e2f)


📌 **Project Overview**

This Document chatbot is a Streamlit-based web application that allows users to upload PDF documents and ask questions based on their contents. The application leverages LangChain, FAISS for vector storage, and Groq's Gemma model for intelligent responses.


🚀 **Features**

Upload PDF Files: Users can upload multiple PDFs for processing.

Vector Store Creation: The application converts documents into embeddings and stores them in a FAISS vector database.

Question Answering: Users can ask questions related to the uploaded documents, and the system retrieves relevant context to generate accurate responses.

Efficient Retrieval: Uses FAISS and LangChain retrieval mechanisms for fast information lookup.

Groq AI Model: The chatbot is powered by Groq's mixtral-8x7b-32768 model for accurate text generation.



🛠️ **Tech Stack**

Frontend: Streamlit

Backend: Python

AI & NLP: LangChain, Google Generative AI Embeddings, FAISS

Cloud APIs: Groq API, Google API

Document Processing: PyPDFDirectoryLoader


📌 **How to Use**

Upload PDFs: Click on the sidebar to upload your documents.

Create Vector Store: Click the "Create Vector Store" button to process the documents.

Ask Questions: Enter your question in the text input field and submit.

View Responses: The system retrieves relevant document snippets and provides an AI-generated answer.


🤝**Contributions**

Feel free to contribute! Open a pull request or submit an issue 
