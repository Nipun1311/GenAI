from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate
import json

load_dotenv()
model = "models/gemini-2.5-flash"
llm = ChatGoogleGenerativeAI(model=model, temperature=0)


st.header("Reasearch Tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis",
    ],
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"],
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)",
    ],
)

# template

with open("template.json", "r") as f:
    data = json.load(f)
template = PromptTemplate.from_template(data["template"])

if st.button("Summarize"):
    st.write("Summarizing your query...")
    chain = template | llm # chain the template and llm
    response = chain.invoke( # invoke the chain
        {                # pass the following arguments to the chain
            "paper_input": paper_input, 
            "style_input": style_input,
            "length_input": length_input,
        }
    )
    st.write(response.content)