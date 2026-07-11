from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# from langchain_core.messages import HumanMessage 
# chat template

chat_template = ChatPromptTemplate(
    [
        ("system", "You are a helpful assistant that answers questions based on the provided context."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", '{query}'),
    ]
)

# load chat history
chat_history = []
with open("chathistory.txt", "r") as f:
    chat_history.extend(f.readlines())
print(chat_history)
print()
# create prompt
prompt = chat_template.invoke({'chat_history': chat_history, 'query':"Tell me about langchain prompts"})
print(prompt)