# local open source embedding
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents=["What is the capital of India?", "What is the capital of China?"]

vector = embeddings.embed_documents(documents)
print(str(vector))
