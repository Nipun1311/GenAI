from langchain_huggingface import HuggingFacePipeline
from langchain_huggingface import ChatHuggingFace

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens=100,
        temperature=0.5,
    )
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("What is the capital of India?")

print(response.content)

