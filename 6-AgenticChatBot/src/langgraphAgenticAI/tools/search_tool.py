from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Returns a list of tools to be used in the agentic chatbot.
    """
    tavily_search_tool = TavilySearchResults()
    tools = [tavily_search_tool]
    return tools

def create_tool_nodes(tools):
    """
    Creates ToolNode instances for each tool in the provided list.
    """
    tool_nodes = []
    for tool in tools:
        tool_node = ToolNode(tool)
        tool_nodes.append(tool_node)
    return tool_nodes