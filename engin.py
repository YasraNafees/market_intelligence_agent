import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import PromptTemplate # ReAct ke liye PromptTemplate behtar hai
from langchain.agents import create_react_agent, AgentExecutor

load_dotenv()

# 1. The Brain: Groq
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

# 2. The Tools: Tavily
search_tool = TavilySearchResults(k=3)
tools = [search_tool]

# 3. Professional ReAct Prompt (Standard Industry Template)
# NOTE: {tools} and {tool_names} are REQUIRED for ReAct agents
template = """Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Business Intelligence Persona: 
You are a Professional Business Intelligence Agent. Your goal is to solve the 'Time-to-Insight' problem.
Identify latest AI projects, hiring trends, and provide strategic recommendations in Markdown.

Question: {input}
Thought: {agent_scratchpad}"""

prompt = PromptTemplate.from_template(template)

# 4. Create the Agent & Executor
# Ab ye error nahi dega kyunke prompt mein variables poore hain
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True, 
    handle_parsing_errors=True,
     max_iterations=3,           # <--- Ye safety lock hai (API bachane ke liye)
    early_stopping_method="force"
)

def run_research(query: str):
    return agent_executor.invoke({"input": query})

if __name__ == "__main__":
    test_query = "Research the latest AI initiatives of 10Pearls and their hiring trends."
    print("\n--- Starting Research ---\n")
    response = run_research(test_query)
    print("\n--- FINAL BUSINESS REPORT ---\n")
    print(response["output"])
