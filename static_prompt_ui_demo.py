from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
llm = ChatOpenAI(model = "gpt-4o", temperature=0.5,max_tokens= 1000)
st.header("Reseach AI Tool Static Prompt Demo")

user_input = st.text_input("Enter your research query")

if st.button("Generate Response"):
    response = llm.invoke(user_input)
    st.write(response.content)
