from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dl-curriculum.pdf')
documents = loader.load()

splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=5,separator="")
# overlap is the number of characters to overlap between chunks
docs = splitter.split_documents(documents)
print(docs[0].page_content)
