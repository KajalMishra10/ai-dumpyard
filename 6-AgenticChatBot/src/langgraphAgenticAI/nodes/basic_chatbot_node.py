from src.langgraphAgenticAI.state.state import State

class BasicChatbotNode:
    """
    A basic chatbot node that processes user input and generates responses.
    """

    def __init__(self, model):
        self.llm = model

    def process_input(self, state: State) -> str:
        """
        Processes the user input from the state and generates a response using the LLM.

        Args:
            state (State): The current state of the agentic AI system.
        Returns:
            str: The generated response from the LLM.
        """ 
        return {"messages":self.llm.invoke(state["messages"])}