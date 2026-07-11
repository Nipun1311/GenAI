from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

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

templete2 = PromptTemplate(
    template="Write a 5 line summary on {text}",
    input_variables=["text"]
)

prompt1 = template1.format(
    topic="Telugu(Tollywood) film Industry's biggest Fanwars with examples"
)

result1 = model.invoke(prompt1)

print(result1.content)
print()

prompt2 = templete2.format(
    text=result1.content
)

result2 = model.invoke(prompt2)

print(result2.content)