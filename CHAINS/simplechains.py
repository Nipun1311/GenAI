from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=["topic"]
    )

model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)

parser = StrOutputParser()

chain = prompt | model | parser # | use of this is called Langchain Expression Language

# response = chain.invoke({"topic": "Sunrisers Hyderabad"})

# print(response)

chain.get_graph().print_ascii()