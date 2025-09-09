from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt1 = PromptTemplate(
    template =' Generate a detailed report on {topic}',
    input_variable= ['topic']

)


prompt2 = PromptTemplate(
    template =' Generate a 5 pointer summary on the following text \n {text}',
    input_variable= ['text']

)


model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':'Bollywood'})

chain.get_graph().print_ascii()
print(result)