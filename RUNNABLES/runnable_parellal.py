from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a tweet about {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Write a LinkedIn post about {topic}", input_variables=["topic"]
)
model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)

parser = StrOutputParser()

chain = RunnableParallel(
    {
        "twitter": RunnableSequence(prompt1, model, parser),
        "linkedin": RunnableSequence(prompt2, model, parser),
    }
)

result = chain.invoke({"LangChain Runnables"})

print(result["twitter"])
print()
print()
print()
print(result["linkedin"])