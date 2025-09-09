from langchain_openai import ChatOpenAI
from pydantic import BaseModel,Field
from typing import Literal
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda,RunnableBranch
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
load_dotenv()


model = ChatOpenAI()
parser = StrOutputParser()

class Feedback(BaseModel):

    sentiment : Literal['positive','negative'] = Field(description= 'Give the sentiment of the feedback')



parser2 = PydanticOutputParser(pydantic_object = Feedback)

prompt1 = PromptTemplate(
    template ='Classify the sentiment of the following feedback text into positive and negative \n{feedback} \n {format_instructions}',
    input_variable= ['feedback'],
    partial_variables = {'format_instructions': parser2.get_format_instructions()}

)


classifier_chain = prompt1 | model | parser2



prompt2 = PromptTemplate(
    template ='Write an appropriate response for this positive feedback \n{feedback} ',
    input_variable= ['feedback']

)

prompt3 = PromptTemplate(
    template ='Write an appropriate response for this negative feedback \n{feedback} ',
    input_variable= ['feedback']
)



branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

chain = classifier_chain | branch_chain

chain.get_graph().print_ascii()

print(chain.invoke({'feedback': 'This is a beautiful phone'}))

