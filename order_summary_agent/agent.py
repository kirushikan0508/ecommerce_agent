from google.adk.agents import Agent

order_summary_agent = Agent(
    name="order_summary_agent",
    description="an order summary agent that gives a summary of the complete order",
    model="gemini-2.5-flash",
    instruction="""
    goal:
    -read the complete order information from session state
    -present a clear, friendly summary of the order to the user.

    use the following information from the state object
    and generte an order summary. the summary should be user friendly and should look like how amazon or flipkart generate them

    {name} {email} {mobile} 
    {item} {quantity} {price} {shipping_address}

    rules:
    read only from state: do not invent random information that are not in state.
    """
)