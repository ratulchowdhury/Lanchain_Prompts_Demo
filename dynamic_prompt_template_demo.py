from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, load_prompt
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

llm = ChatOpenAI(model = "gpt-4o", temperature=0.5,max_tokens= 1000)
st.header("Research AI Tool Dynamic Prompt Demo")   

paper_input = st.selectbox("Select the name of the research paper",\
    ["Attention is All You Need", \
        "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",\
            "GPT-3: Language Models are Few-Shot Learners"])

style_input = st.selectbox("Select the style of the summary",\
    ["Theory Oriented", "Implementation Oriented", "Mathematics Oriented"])

input_length = st.slider("Select the length of the summary", 500, 750, 1000, step=250)

prompt_template = load_prompt("prompt_template.json")

if st.button("Generate Response"):
    chain = prompt_template | llm
    response = chain.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": input_length
    })
    st.write(response.content)
