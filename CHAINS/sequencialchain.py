from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a detailed report about {topic}",
    input_variables=["topic"]
    )

prompt2 = PromptTemplate(
    template="Write a 5 line summary on {text}",
    input_variables=["text"]
    )

model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

response = chain.invoke({"topic": "Indian Premier League"})

print(response)

chain.get_graph().print_ascii()