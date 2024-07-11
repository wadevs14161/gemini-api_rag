from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS

GOOGLE_API_KEY = "AIzaSyC51i2oLCOHgZ5X0hLfSr65lKdaE0KrpDQ"

genai.configure(api_key=GOOGLE_API_KEY)


def get_vector_store(chunks, dbname: str):
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    vector_store.save_local(dbname)