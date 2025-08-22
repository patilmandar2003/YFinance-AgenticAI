# Import necessary libraries from the agno framework
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools

# dotenv is used to store and load sensitive information like API keys in .env file.
from dotenv import load_dotenv

# Used to interact with OS and fetch environment variables
import os

# Load the environment variables from the .env file.
# This must be called at the beginning of the script before
# you try to access any variables from os.getenv().
load_dotenv()

# --- Step 1: Initialize the Model and Tools ---
# The model is the "brain" of the agent. It handles the reasoning and decision-making.
# We're using Gemini 2.5 Flash here, which is a fast and efficient model.
# The `id` parameter specifies the Gemini model you want to use.
# It's good practice to get the API key from a secure environment variable.
try:
    # Use os.getenv() to retrieve the value of the GEMINI_API_KEY environment variable.
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file. Please set it.")
    
    # Initialize the Gemini model with the specific model ID and your API key.
    # The `id` should be 'gemini-2.5-flash-preview-05-20' or a similar model ID.
    model = Gemini(id="gemini-2.5-flash-preview-05-20", api_key=gemini_api_key)

except Exception as e:
    print(f"Error initializing Gemini Model: {e}")
    exit()

# The tools are the "hands" of the agent, allowing it to interact with the real world.
# ReasoningTools give the agent the ability to think step-by-step before answering.
reasoning_tools = ReasoningTools(add_instructions=True)

# YFinanceTools give the agent the ability to fetch financial data from Yahoo Finance.
# You can customize which tools are enabled (e.g., historical prices, company news).
y_finance_tools = YFinanceTools(
    stock_price=True,
    historical_prices=True,
    company_info= True,
    analyst_recommendations=True,
    company_news=True
)

# A list of all tools the agent can use.
tools = [reasoning_tools, y_finance_tools]

# The 'instructions' parameter is an optional list of rules that constrain the agent's
# final output. These rules are used to force the agent to format its response
# in a specific way, for example, to only use tables or to exclude any extra text.
instructions=[
    "Use only tables to display the data.",
    "Only output the report, no other text."]

# --- Step 2: Create the Agent ---
# The Agent class orchestrates everything. It connects the model with the tools.
# The `description` parameter is a crucial system prompt that defines the agent's persona and purpose.
# The `show_tool_calls=True` setting is great for debugging as it shows the agent's thought process.
agent = Agent(
    model=model,
    tools=tools,
    instructions=instructions,
    description="""
    You are a professional financial analyst. Your purpose is to analyze the stock market
    for specific companies and provide a comprehensive report based on your analysis.
    You have access to tools that can fetch financial data. You must use these tools
    to gather information before providing your final answer.""",
    show_tool_calls=True,
    markdown=True,
)

# --- Step 3: Run the Agent with a Task ---
# The agent's `print_response` method is used to get a response for a given query.
# It will automatically use the model and tools to fulfill the request.
# Let the agent analyze a company. This task requires it to use both tools:
# YFinanceTools to get the data, and ReasoningTools to analyze it.
agent.print_response(
    message="Write a report on NVDA.",
    stream=True,
    show_full_reasoning=True,
    stream_intermediate_steps=True
)