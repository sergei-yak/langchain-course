import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()  # take environment variables from .env.


def main():
    print("Hello from langchain-course!")
    information = """
Elon Reeve Musk FRS (born June 28, 1971) is a businessman and entrepreneur. He moved to Canada and later became a U.S. citizen. He was the Commissioner of the Department of Government Efficiency for a few months in 2025 during the second Donald Trump administration.[1] He became rich through several technology projects, including an online finance company which merged with PayPal in the year 2000.[2] Musk has been the wealthiest person in the world since 2021, according to both the Bloomberg Billionaires Index and Forbes's real-time billionaires list; with a net worth of US$932 billion according to Bloomberg and $912 billion according to Forbes as of July 8, 2026.[3][4] Upon the stock market debut of his company SpaceX in June 2026, Musk became the first person to ever become a trillionaire in terms of US dollars.[5] In 2021, he was Time Person of the Year.
Elon is the current CEO and Chief Product Architect of Tesla, Inc., a company that makes electric vehicles. He is also the CEO and CTO of SpaceX, an aerospace company. In 2022, he became the owner of the social media site Twitter which he later gave a new name known as X after buying it for USD $44 billion.
In November 2024, U.S. President-elect Donald Trump said that Musk would become a leader of the Department of Government Efficiency (DOGE)[8] alongside Vivek Ramaswamy but Ramaswamy stepped down before the Department was created.

    """
    summary_template = """
Given the information {information} about a person I want you to create:
1. A short summary
2. Two interesting facts about them
"""
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    llm = ChatOpenAI(model_name="gpt-5",temperature=0,openai_api_key=os.environ.get("OPENAI_API_KEY"),)
    #llm = ChatOllama(temperature=0, model="qwen3.8:latest")
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response.content)


if __name__ == "__main__":
    main()
