from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    dimensions=32
)
documents=["What is the capital of India?", "What is the capital of China?"]

vector = embedding.embed_documents(documents)
print(vector)
