from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)

model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)

parser = StrOutputParser()

report_generator = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x:len(x.split()) > 100, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
    )

final_chain = RunnableSequence(report_generator, branch_chain)

print(final_chain.invoke({'topic':'Russia vs Ukraine'}))