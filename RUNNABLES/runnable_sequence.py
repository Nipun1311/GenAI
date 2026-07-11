from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
    )

prompt2 = PromptTemplate(
    template="Print the {text} and then explain the joke {text}",
    input_variables=["text"]
)

model = ChatGroq(model="llama-3.3-70b-versatile", temperature=1.5)

parser = StrOutputParser()

chain = RunnableSequence(prompt, model, parser, prompt2, model, parser)

result = chain.invoke({"topic": "RCB 49 all out"})

print(result)
