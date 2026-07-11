import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
)

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
)

st.title("🤖 Groq Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask anything..."):

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # -------- Create LangChain message list --------

    messages = [
        SystemMessage(
            content=(
                "You are a helpful AI assistant. "
                "Always answer in English. "
                "Be concise unless the user asks for more detail."
            )
        )
    ]

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            messages.append(HumanMessage(content=msg["content"]))
        else:
            messages.append(AIMessage(content=msg["content"]))

    # -------- Invoke LLM --------

    response = model.invoke(messages)

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response.content)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.content,
        }
    )