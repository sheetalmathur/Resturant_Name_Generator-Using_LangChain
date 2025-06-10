
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
import os

os.environ["OPENAI_API_KEY"]= "KEY"
llm = OpenAI(temperature=0.6)


def generate_resturant_name_and_items(cuisne):
    prompt_template_name = PromptTemplate(
        input_variables=['cusine'],
        template="I want to open a restaurant for {cusine} food. Suggest a fancy name for this."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="resturant_name")

    prompt_template_items = PromptTemplate(
        input_variables=['resturant_name'],
        template="Suggest some menu items for {resturant_name}. Return it as comma separated."
    )

    # Fixed output_key to match in final chain
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=["cusine"],
        output_variables=["resturant_name", "menu_items"],
        verbose=True
    )

    # Run the chain
    response = chain({"cusine": cuisne})
    return response

