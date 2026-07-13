from langchain_community.document_loaders import WebBaseLoader
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
    template="Answer the following question:\n{question} from the following text: {text}",
    input_variables=["question", "text"]
)

parser = StrOutputParser()



url = "https://docs.langchain.com/"
loader = WebBaseLoader(url)
documents = loader.load()

chain = prompt | model | parser
result = chain.invoke({"question": "What is LangChain?", "text": documents[0].page_content})
print(result)

