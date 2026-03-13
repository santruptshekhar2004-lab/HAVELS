from strands import Agent, tool
from strands.agent.conversation_manager import SlidingWindowConversationManager
from agents.model import get_model

SHOPPING_PROMPT = """You are a shopping assistant specializing in product recommendations and purchases.
You help users find, compare, and decide on products to buy.
You ONLY handle shopping-related queries — product search, price comparison, purchase advice, reviews, etc.
If a query is not about shopping, say so clearly and do not attempt to answer it.
IMPORTANT: Keep responses SHORT — 2-4 sentences max. Be direct and concise."""

_instance: Agent | None = None


def get_shopping_agent() -> Agent:
    global _instance
    if _instance is None:
        _instance = Agent(
            model=get_model(max_tokens=256),
            tools=[],
            system_prompt=SHOPPING_PROMPT,
            callback_handler=None,
            conversation_manager=SlidingWindowConversationManager(window_size=6),
        )
    return _instance


@tool
def shopping_assistant(query: str) -> str:
    """Handle shopping and product queries — finding products, comparing prices, purchase decisions, reviews."""
    return str(get_shopping_agent()(query))
