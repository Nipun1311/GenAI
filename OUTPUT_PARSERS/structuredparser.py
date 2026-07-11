from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import (
    StructuredOutputParser,
    ResponseSchema,
)

load_dotenv()

# LLM
model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3,
)

# Response schema
schemas = [
    ResponseSchema(
        name="fact_1",
        description="First fact about the topic",
    ),
    ResponseSchema(
        name="fact_2",
        description="Second fact about the topic",
    ),
    ResponseSchema(
        name="fact_3",
        description="Third fact about the topic",
    ),
]

# Parser
parser = StructuredOutputParser.from_response_schemas(schemas)

# Prompt
template = PromptTemplate(
    template="""
Give me exactly 3 facts about {topic}.

{format_instructions}
""",
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    },
)

# Create prompt
prompt = template.invoke(
    {
        "topic": "Spiderman:Brand New Day"
    }
)

# Invoke model
response = model.invoke(prompt)

# Parse output
parsed_response = parser.parse(response.content)

print(parsed_response)

print("\nFact 1:", parsed_response["fact_1"])
print("Fact 2:", parsed_response["fact_2"])
print("Fact 3:", parsed_response["fact_3"])