from google.adk import Agent
from google.adk.tools import ToolContext
from order_summary_agent.agent import order_summary_agent

def save_shipping_address(tool_context: ToolContext,
                          address:str):
    tool_context.state["shipping_address"] = address

checkout_agent = Agent(
    name="checkout_agent",
    description="A checkout agent that collect user's shipping address",
    model="gemini-2.5-flash",
    instruction="""
    you are checkout agent.

    goal:
    -collect the user's shipping address.
    -use the save_shipping address to save the shippling address into the session state.
    -then check with the user if they want to view their order summary and transfer to the order_summary agent.
    """,
    tools=[save_shipping_address],
    sub_agents=[order_summary_agent]
)