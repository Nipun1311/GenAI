from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template="Write a detailed report about {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Write a detailed summary on {text}",
    input_variables=["text"]
)

pareser = StrOutputParser()

chain = template1 | model | pareser | template2 | model | pareser

response = chain.invoke(
    {
        "topic": "Telugu(Tollywood) film Industry's 5 biggest Fanwars with examples"
    }
)

print(response)