from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

# RunnableParallel is a class that is used to run multiple chains in parallel.

load_dotenv()

model1 = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)

model2 = llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="Give the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback as positive or negative \n {feedback} \n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
    )

classifier = prompt1 | model1 | parser2  

prompt2 = PromptTemplate(
    template="Write an appropriate response to the positive feedback \n {feedback} ",
    input_variables=["feedback"]
    )

prompt3 = PromptTemplate(
    template="Write an appropriate response to the negative feedback \n {feedback} ",
    input_variables=["feedback"]
    )

branch = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model1 | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model1 | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)
chain = classifier | branch

result = chain.invoke({"feedback": "This is a terrible Smartphone"})    

print(result)
