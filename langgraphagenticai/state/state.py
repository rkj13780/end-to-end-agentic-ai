from typing import Annotated, Literal, Optional
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from typing import TypedDict, Annotated, List
from langchain_core.messages import HumanMessage, AIMessage

class State(TypedDict):
    """
    Represents the structuer of the state used in the graph
    """
    add_messages: Annotated[list, add_messages]