from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
import json
import os
load_dotenv()

llm = ChatOpenAI(model = "gpt-4o", temperature=0.5, max_tokens=1000)

chat_prompt = ChatPromptTemplate([
    ("system", "You are a customer support agent of Pizzanos restaurant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{user_input}")
])

history = []

# Load chat history from file if it exists
if os.path.exists("chat_history.json"):
    try:
        with open("chat_history.json", "r") as f:
            history_data = json.load(f)
            for msg in history_data:
                if msg["type"] == "human":
                    history.append(HumanMessage(content=msg["content"]))
                elif msg["type"] == "ai":
                    history.append(AIMessage(content=msg["content"]))
    except (json.JSONDecodeError, KeyError):
        print("Error loading chat history. Starting with fresh history.")
        history = []

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "exit":
        print("Chat History:", history)
        # Save chat history to JSON file
        history_data = []
        for message in history:
            if isinstance(message, HumanMessage):
                history_data.append({"type": "human", "content": message.content})
            elif isinstance(message, AIMessage):
                history_data.append({"type": "ai", "content": message.content})
        
        with open("chat_history.json", "w") as f:
            json.dump(history_data, f, indent=2)
        print("Chat history saved to chat_history.json")
        break
    
    # Use the chat prompt template with history
    formatted_prompt = chat_prompt.format_messages(history=history, user_input=user_input)
    response = llm.invoke(formatted_prompt)
    
    # Add user message and AI response to history
    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=response.content))
    
    print("AI:", response.content)