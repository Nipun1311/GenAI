from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.prompts import SystemMessage, HumanMessage, AIMessage

chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful {domain} Expert."
         "Always answer in English."
         "Be concise unless the user asks for more detail."),
         ("user", "Explain in simple terms about {topic}")
    ]
)
# this cannot be used because it is not a list of messages
    #     SystemMessage(
    #         content="You are a helpful {domain} Expert."
    #         "Always answer in English."
    #         "Be concise unless the user asks for more detail."
    #     ),
    #     HumanMessage(content="Explain in simple terms about {topic}")
    # ]
    # )
prompt = chat_prompt.invoke(
    {
        "domain":"Finance", 
        "topic":"Stock Market"
    }
)

print(prompt)