from src.langgraphAgenticAI.state.state import State

class ChatbotWithToolsNode:
    def __init__(self, llm):
        self.llm = llm

    def process_input(self, state: State) -> State:
        # Process the input using the LLM and tools
        # This is a placeholder for the actual implementation
        return {"messages":self.llm.invoke(state["messages"])}

    def create_chatbot(self,tools):
        llm_with_tools = self.llm.bind_tools(tools)  # Placeholder for LLM with tools integration
        def chatbot_function(state: State) -> State:
            return {"messages":llm_with_tools.invoke(state["messages"])}
        return chatbot_function