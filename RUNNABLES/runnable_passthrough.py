from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
    )

prompt2 = PromptTemplate(
    template="Explain the joke {text}",
    input_variables=["text"]
)

model = ChatGroq(model="llama-3.3-70b-versatile", temperature=1.5)

parser = StrOutputParser()

joke_generator = RunnableSequence(prompt, model, parser)

parellal_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "explainer": RunnableSequence(prompt2, model, parser),
    }
)

final_chain = RunnableSequence(joke_generator, parellal_chain)
result = final_chain.invoke({"topic": "IPL 2023"})

print(result)