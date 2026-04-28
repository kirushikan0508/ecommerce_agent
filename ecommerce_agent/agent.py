from google.adk import Agent
from google.adk.tools import ToolContext
from catalog_agent.agent import catalog_agent

def save_user_info(tool_context: ToolContext,
                   name:str,
                   email:str,
                   mobile:str):
    tool_context.state["name"] = name
    tool_context.state["email"] = email
    tool_context.state["mobile"] = mobile

root_agent = Agent(
    name="ecommerce_agent",
    description="An ecommerce agent that manages the ecommerce workflow",
    model="gemini-2.5-flash",
    instruction="""
    Role= you are an ecommerce agent who can help the user with product catolog, checkout and order tracking
    
    workflow:
    -greet the user and a brief introduction about your self on how can you help and then start the user details as mentioned below. do not directlt start gathering user information.
    -if you do not know, ask for the user's name, email and mobile number. ask only one information at a time
    -once you have the above information, call the save_user_info() tool to save these information.
    -then understand the user's intent. are they looking for new purchase or track existing order.
    -based on the user's request and route it to ONE of your sub-ahents:
        -catolog-agent- for new purchases, questions about products, prices, availablity etc.
        -checkout_agent - for checkout of items in cart.
        -tracking_agent - for tracking existing orders.
    
        Rules:
        1.never answer the question your self. always delegate to exactly one sub-agents.
        2.of user's message clearly matches one category, immediately call that agent.
        3.if you unsure, ask a short claifying questions instead of guesing.
        4.after a sub-agent responds, you may send that response back as-is to the user, without adding extra content.
    """,
    tools=[save_user_info],
    sub_agents=[catalog_agent]
)