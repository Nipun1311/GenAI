from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1.5,
    max_completion_tokens=10
) #temperature is the randomness of the output  0 is lowest and 1 is highest

response = llm.invoke("Write a poem about cricket in 5 lines")

print(response.content)
