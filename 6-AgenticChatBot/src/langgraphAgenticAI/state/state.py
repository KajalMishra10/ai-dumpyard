from typing_extensions import Annotated, TypedDict
from langgraph.graph.message import add_messages

class State(TypedDict):
    """
    Represents the state of the agentic AI system.
    """
    messages: Annotated[list, add_messages]  # List of messages in the state