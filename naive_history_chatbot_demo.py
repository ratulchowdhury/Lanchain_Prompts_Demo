from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


llm = ChatOpenAI(model = "gpt-4o", temperature=0.5,max_tokens= 1000)
history = []


while True:
    user_input = input("You:")
    history.append(user_input)
    if user_input == "exit":
        break
    response = llm.invoke(history)
    history.append(response.content)
    print("AI:", response.content)