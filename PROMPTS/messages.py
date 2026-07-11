from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3
)

messages = [
    SystemMessage(
        content="You are a helpful assistant that answers questions based on the provided context."
    ),
    HumanMessage(content="Tell me about langchain and its features.")
]

response = model.invoke(messages)

messages.append(AIMessage(content=response.content))

print (messages)