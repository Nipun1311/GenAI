from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()



prompt1 = PromptTemplate(
    template="Write a tweet about {topic}", input_variables=["topic"]
)

model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)

parser = StrOutputParser()

joke_generator = RunnableSequence(prompt1, model, parser)

parellal_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "word_count": RunnableLambda(lambda x: len(x.split())),
    }
)

final_chain = RunnableSequence(joke_generator, parellal_chain)

result = final_chain.invoke({"topic": "IPL 2023"})

print(result)