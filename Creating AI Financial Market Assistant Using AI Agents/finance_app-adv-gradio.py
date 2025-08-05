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

# Web agent
web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    instructions="Always include sources",
    show_tool_calls=True,
    markdown=True,
)

# Finance agent
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

# Team of agents
agent_team = Agent(
    team=[web_agent, finance_agent],
    model=OpenAIChat(id="gpt-4o"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# Main function
def chat_with_agents(stock_choice, custom_stock, analysis_type, time_horizon, custom_question):
    selected_stock = custom_stock if custom_stock else stock_choice
    prompt = f"{custom_question} about {selected_stock}. Please focus on {analysis_type} over a {time_horizon} horizon."
    result = agent_team.run(prompt)
    return result.content if hasattr(result, "content") else str(result)

# Stock options
stock_options = ["Tesla", "Apple", "Amazon", "Nvidia", "Microsoft", "Meta"]
analysis_types = ["Fundamental Analysis", "Technical Analysis", "Market Sentiment", "News Impact"]
time_horizons = ["Short-term", "Medium-term", "Long-term"]

# Layout UI
title = "<h1 style='text-align: center;'>AI Financial Market Assistant</h1>"
logo_url = "https://raw.githubusercontent.com/Decoding-Data-Science/airesidency/main/dds_logo.jpg"

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown(title)
    with gr.Row():
        with gr.Column(scale=1):
            gr.Image(value=logo_url, show_label=False, interactive=False, elem_id="dds-logo", height=300, width=300)
            stock_dropdown = gr.Dropdown(choices=stock_options, label="Choose a Stock", value="Tesla")
            custom_stock_box = gr.Textbox(lines=1, label="Or enter a custom stock symbol")
            analysis_dropdown = gr.Dropdown(choices=analysis_types, label="Type of Analysis", value="Fundamental Analysis")
            horizon_dropdown = gr.Dropdown(choices=time_horizons, label="Time Horizon", value="Medium-term")
            question_box = gr.Textbox(lines=2, label="Enter your question", placeholder="Should I buy, hold, or sell?")
            submit_btn = gr.Button("Analyze")
        with gr.Column(scale=2):
            response_output = gr.Markdown()

    submit_btn.click(
        fn=chat_with_agents,
        inputs=[stock_dropdown, custom_stock_box, analysis_dropdown, horizon_dropdown, question_box],
        outputs=response_output
    )

demo.launch(share=True)
