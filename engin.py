import os
import asyncio
from langchain.memory import ConversationTokenBufferMemory
from typing import List
from dotenv import load_dotenv
from pydantic import BaseModel, Field

from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import PromptTemplate
from langchain.agents import create_react_agent, AgentExecutor
from langchain.output_parsers import PydanticOutputParser, OutputFixingParser

load_dotenv()

# 1. Model Setup (Stable version)
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

# 2. Tools & Schema
search_tool = TavilySearchResults(k=3, include_raw_content=False)
tools = [search_tool]

class BIReport(BaseModel):
    company_name: str = Field(description="Name of the company")
    latest_project: List[str] = Field(description="List of AI initiatives")
    hiring_trends: str = Field(description="Summary of hiring")
    strategic_advice: str = Field(description="Markdown formatted advice")

base_parser = PydanticOutputParser(pydantic_object=BIReport)
fixing_parser = OutputFixingParser.from_llm(parser=base_parser, llm=llm)
format_instruction = base_parser.get_format_instructions()

# Memory: Token-based management for stability
memory = ConversationTokenBufferMemory(llm=llm, max_token_limit=2000, memory_key="chat_history")

# --- 3. Optimized Prompt for History Preservation ---
template = """You are a Senior Business Intelligence Analyst. 
Your goal is to build a COMPREHENSIVE report by combining new research with existing data from the chat history.

STRICT RULES:
1. CHECK CHAT HISTORY: Before searching, review the {chat_history}. If data already exists, DO NOT delete it.
2. MERGE DATA: When providing the Final Answer, combine newly found facts with the information already present in the history.
3. NO HALLUCINATION: Use only real data from tools. Never use dummy names like 'ABC Corp'.
4. PERSISTENCE: Ensure the 'latest_project' list grows as new projects are discovered across multiple turns.

TOOLS:
{tools}

FORMAT:
Thought: I should check history first, then search for new details.
Action: {tool_names}
Action Input: "latest AI projects and hiring trends for [Company]"
Observation: [Tool Output]
...
Thought: I will now merge the history and new findings into the final JSON.
Final Answer: 
{format_instruction}

CHAT HISTORY SO FAR:
{chat_history}

Question: {input}
Thought: {agent_scratchpad}"""

prompt = PromptTemplate(
    template=template,
    input_variables=["input", "agent_scratchpad", "tools", "tool_names", "chat_history"],
    partial_variables={"format_instruction": format_instruction}
)

# 4. Agent Configuration
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True,
    handle_parsing_errors="ERROR: Return ONLY a valid JSON object matching the schema.",
    max_iterations=8, 
    early_stopping_method="force"
)

async def run_research(query: str):
    print("Waiting for Rate Limit (30s)...")
    await asyncio.sleep(30) 
    
    response = await agent_executor.ainvoke({"input": query})
    
    raw_output = response["output"]
    # Clean possible 'Final Answer:' prefix
    if "Final Answer:" in raw_output:
        raw_output = raw_output.split("Final Answer:")[-1].strip()
    
    try:
        return fixing_parser.parse(raw_output)
    except Exception as e:
        print(f"Parsing failed: {e}")
        return raw_output

if __name__ == "__main__":
    test_query = "Research the latest AI initiatives of 10Pearls and their hiring trends."
    result = asyncio.run(run_research(test_query))
    print("\n--- FINAL CLEAN REPORT ---\n")
    print(result)
