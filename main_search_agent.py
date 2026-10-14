from dotenv import load_dotenv
load_dotenv() # load environment variables from .env file
from langchain.agents import create_agent
from langchain.tools import tool # tool decorator
from langchain_core.messages import HumanMessage # we will use HumanMessage to invoke an agent
from langchain_openai import ChatOpenAI
#from tavily import TavilyClient
from langchain_tavily import TavilySearch # we imported already prebuilt TavilySearch tool from langchain_tavily package, so we don't need to use TavilyClient directly


#tavily = TavilyClient()


llm = ChatOpenAI()
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the Dallas area on linkedin and list their details")})
    print(result)












if __name__ == "__main__": # if this script is run directly (not imported as a module)
    main()