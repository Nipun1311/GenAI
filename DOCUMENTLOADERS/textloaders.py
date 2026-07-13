from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3,
)

prompt= PromptTemplate(
    template="Write a summary for the following text: {poem}",
    input_variables=["poem"]
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt', encoding='utf-8')
documents = loader.load()
# print(type(documents))
# print(len(documents))
# print(documents[0].page_content)
# print(documents[0].metadata)

# all the document loaders give the output in the form of a list of documents

chain = prompt | model | parser
result = chain.invoke({"poem": documents[0].page_content})
print(result)