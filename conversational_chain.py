from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain

def get_conversational_chain(db_index):
    # prompt_template = """
    # You are a CSV data assistant. Your task is to assist users in retrieving information from the provided CSV file. Your goal is to provide accurate answers based on the context of the data. If the answer is not available in the provided context, you should indicate that to the user.
    # Use the provided context and question to generate an accurate response. If you encounter any issues or uncertainties, feel free to seek clarification or provide suggestions for refining the query.
    
    # Context:\n {context}?\n
    # Question: \n{question}\n

    # Answer:
    # """
    prompt_courses = """
    你的任務是從用戶輸入的訊息中，提取關鍵字，比對向量資料庫，並推薦三到五門課程給用戶，課程連結為必要資訊。
    請使用繁體中文回答。

    上下文:\n {context}?\n
    問題: \n{question}\n

    答案:
    """

    prompt_welfare = """
    你的任務是從用戶輸入的訊息中，提取關鍵字，比對向量資料庫，並提供三到五個就業補助方案給用戶。
    請使用繁體中文回答。

    上下文:\n {context}?\n
    問題: \n{question}\n

    答案:
    """

    if db_index == "laborBenefit_index":
        prompt_template = prompt_welfare
    elif db_index == "faiss_index":
        prompt_template = prompt_courses
    # prompt_template = """
    # You are a CSV data assistant. Your task is to assist users in retrieving information from the provided CSV file.
    # Your goal is to provide several courses based on the user's input. You should extract relevant course information from the user's input and recommend three to five courses to the user.

    # Context:\n {context}?\n
    # Question: \n{question}\n

    # Answer:
    # """

    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest",
                                   client=genai,
                                   temperature=0.8,
                                   top_k=10,
                                   )
    prompt = PromptTemplate(template=prompt_template,
                            input_variables=["context", "question"])
    chain = load_qa_chain(llm=model, chain_type="stuff", prompt=prompt)
    return chain


if __name__ == "__main__":
    pass