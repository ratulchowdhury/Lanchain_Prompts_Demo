from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import json
load_dotenv()

llm = ChatOpenAI(model = "gpt-4o", temperature=0.5,max_tokens= 1000)
history = [(SystemMessage(content="You are as  customer support agent of pizzanos restaurant."))]

while True:
    user_input = input("You:")
    history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        print("Chat History:", history)
        # Save chat history to file
        with open("chat_history.txt", "w") as f:
            for message in history:
                f.write(f"{type(message).__name__}: {message.content}\n")
        print("Chat history saved to chat_history.txt")
        break
    response = llm.invoke(history)
    history.append(AIMessage(content=response.content))
    print("AI:", response.content)