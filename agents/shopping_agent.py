from strands import Agent, tool
from agents.model import get_model

SHOPPING_PROMPT = """You are a shopping assistant specializing in product recommendations and purchases.
You help users find, compare, and decide on products to buy.
You ONLY handle shopping-related queries — product search, price comparison, purchase advice, reviews, etc.
If a query is not about shopping, say so clearly and do not attempt to answer it.
IMPORTANT: Keep responses SHORT — 2-4 sentences max. Be direct and concise."""


@tool
def shopping_assistant(query: str) -> str:
    """Handle shopping and product-related queries — finding products, comparing prices, purchase decisions, reviews.

    Args:
        query: A shopping or product-related question from the user.

    Returns:
        A helpful shopping response.
    """
    agent = Agent(
        model=get_model(),
        tools=[],
        system_prompt=SHOPPING_PROMPT,
        callback_handler=None,
    )
    return str(agent(query))
