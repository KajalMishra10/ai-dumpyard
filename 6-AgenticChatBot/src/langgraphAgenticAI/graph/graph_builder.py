from langgraph.graph import END, START, StateGraph
from src.langgraphAgenticAI.state.state import State
from src.langgraphAgenticAI.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphAgenticAI.tools.search_tool import get_tools, create_tool_nodes
from langgraph.prebuilt import ToolNode, tools_condition
class GraphBuilder:
    def __init__(self, model):
        self.llm=model
        self.graph_builder = StateGraph(State, self.llm)

    def basic_chatbot_build_graph(self, ) -> None:
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process_input)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def chatbot_with_tools_build_graph(self) -> None:
        tools=get_tools()
        tool_nodes=create_tool_nodes(tools)

        llm=self.llm

        self.graph_builder.add_node("chatbot", "")
        self.graph_builder.add_node("tools", tool_nodes[0])
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools","chatbot")
        self.graph_builder.add_edge("chatbot", END)


    def setup_graph(self, usecase: str) -> None:
        if usecase == "basic_chatbot":
           self.basic_chatbot_build_graph()
        if usecase == "chatbot_with_tools":
            self.chatbot_with_tools_build_graph()
            
        return self.graph_builder.compile()