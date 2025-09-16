from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model = "gpt-4o", temperature=0.5,max_tokens= 1000)

chat_prompt=ChatPromptTemplate([
    ("system","You are a {domain} expert."),\
    ("human","Explain the concept of {concept} in a {style} manner.")
    ])
prompt = chat_prompt.invoke({
    "domain":"Football",
    "concept":"3-4-3 Formation",
    "style":"tactical"
})
print(llm.invoke(prompt).content)