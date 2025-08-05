import os
from dotenv import load_dotenv
import gradio as gr

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Web agent to search general web content
web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions="Always include sources",
    show_tool_calls=True,
    markdown=True,
)

# Finance agent to retrieve stock and financial data
finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_info=True
        )
    ],
    instructions="Use tables to display data",
    show_tool_calls=True,
    markdown=True,
)

# Team of agents working together
agent_team = Agent(
    team=[web_agent, finance_agent],
    model=OpenAIChat(id="gpt-4o"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# Gradio function to interface with agents
def chat_with_agents(user_input):
    result = agent_team.run(user_input)
    return result.content if hasattr(result, "content") else str(result)

# Launch Gradio app
gr.Interface(
    fn=chat_with_agents,
    inputs=gr.Textbox(lines=4, placeholder="Ask about Tesla, NVDA, or any market question..."),
    outputs=gr.Markdown(),
    title="📊 DDS AI Financial Market Assistant",
    description="Ask financial, stock, or market-related questions. Powered by GPT-4, web tools, and stock data agents.",
).launch(share=True)
