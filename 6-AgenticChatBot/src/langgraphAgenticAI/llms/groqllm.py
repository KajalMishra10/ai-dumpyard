from langchain_groq import ChatGroq


class GroqLLM:

    def __init__(self, api_key: str, model_name: str):
        self.llm = ChatGroq(
            groq_api_key=api_key,
            model=model_name,
            temperature=0.2
        )

    def generate(self, prompt: str) -> str:
        response = self.llm.invoke(prompt)
        return response.content
    
    def get_llm_model(self):
        return self.llm