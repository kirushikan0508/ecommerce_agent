from google.adk.agents import Agent
from google.adk.tools import ToolContext

def save_cart(tool_context: ToolContext,
              category:str,
              item:str,
              quantity:int,
              price:int):
    tool_context.state[category]=category
    tool_context.state[item]=item
    tool_context.state[quantity]=quantity
    tool_context.state[price]=price


catalog_agent = Agent(
    name="catalog_agent",
    description="A catalog agent that can show products and categories",
    model="gemini-2.5-flash",
    instruction="""
    your scope:
    -answer questions about products, actegories, prices, brands and basic comparisions
    -you can invent a simple fake catalog for demo:
    -smartphones: pixel 9 ($70000), iphone 16 ($80000), samsung s23 ($75000)
    -laptops: macbook pro ($150000), dell xps ($120000), lenovo thinkpad ($100000)
    -headphones: bose 700 ($30000), sony wh-1000xm4 ($25000), airpods pro ($20000)

    workflow:
    -inform the user that you have 3 category of products as mentioned above ask what category they would like to browse
    -then give the details of the products from that category
    -and ask if they want to add any of these items to their shopping cart
    -if yes, get the quntity they want to add store the vatgory, prodiuctas and quantity into the state using save_cart() tool.
    -once you have captured these details, check if the user wants to checkout and then handover to the checkout_agent

    Guidelines:
    1. stay only in catalog domain. do not place orders or track orders.
    2.keep answers short and friendly (2 to 3 sentenses).
    3.if the user asks to "buy), place order or "track delivery", say:
    "this looks like an order or tracking questions. please ask the assistant again, or choose the order/tracking options."
    4.when recommanding products, give at most 3 options and a one-line reason for each.
    5. use simple bullet points where helpful.
  
    """,
    tools=[save_cart]
)