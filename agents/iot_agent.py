from strands import Agent, tool
from agents.model import get_model

IOT_PROMPT = """You are an IoT device control assistant.
You help users manage smart home devices — turning on/off lights, ACs, fans, thermostats, locks, cameras, etc.
You ONLY handle IoT / smart-home device control queries.
If a query is not about controlling or managing IoT devices, say so clearly and do not attempt to answer it.
When a user asks to control a device, confirm the action you would take (e.g. "Turning on the AC in the living room")."""


@tool
def iot_assistant(query: str) -> str:
    """Handle IoT and smart home device control queries — turning devices on/off, adjusting settings, checking device status.

    Args:
        query: An IoT or smart-home device control request from the user.

    Returns:
        A confirmation or status of the device action.
    """
    agent = Agent(
        model=get_model(),
        tools=[],
        system_prompt=IOT_PROMPT,
        callback_handler=None,
    )
    return str(agent(query))
