from dotenv import load_dotenv
from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

text_splitter = SemanticChunker(embeddings, breakpoint_threshold_type="standard_deviation", breakpoint_threshold_amount=1)

text = """
Virat Kohli is one of India's greatest batsmen.
He has scored over 80 international centuries.

Lionel Messi is widely regarded as one of the greatest footballers.
He won the FIFA World Cup with Argentina in 2022.

Python is a popular programming language.
It is widely used in Machine Learning and Artificial Intelligence.
"""

chunks = text_splitter.create_documents([text])
print(len(chunks))
print(chunks)