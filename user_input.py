from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from conversational_chain import get_conversational_chain


def user_input(user_question, db_index):
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001")  # type: ignore

    new_db = FAISS.load_local(db_index, embeddings, allow_dangerous_deserialization=True) 
    docs = new_db.similarity_search(user_question, top_k=10)

    chain = get_conversational_chain(db_index)

    response = chain(
        {"input_documents": docs, "question": user_question}, return_only_outputs=True)

    return response


if __name__ == "__main__":
    # user_question = "我想當水電工"
    user_question = "我是一個二度就業婦女，請問我適用哪些計畫"
    db = "laborBenefit_index"
    response = user_input(user_question, db)
    
    from pprint import pprint
    pprint(response)