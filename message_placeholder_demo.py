from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder



chat_prompt=ChatPromptTemplate([
    ("system","You are as  customer support agent of pizzanos restaurant."),
    MessagesPlaceholder(variable_name="history"),
    ("human","{user_input}")])

history = []

with open("chat_history.txt", "r") as f:
    history.extend(f.readlines())
    
print(history)

prompt =chat_prompt.invoke({
    "history": history,
    "user_input": "When will I get my refund."
})
print(prompt)