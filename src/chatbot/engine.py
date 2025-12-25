from langchain_openai import ChatOpenAI
from config.settings import settings

class ChatbotEngine:
    def __init__(self, api_key: str = None, model: str = None):
        self.api_key = api_key or settings.OPENAI_API_KEY
        self.model = model or settings.MODEL_NAME
        self.llm = None
        
        if self.api_key:
            self.llm = ChatOpenAI(model=self.model, api_key=self.api_key)

    def get_response(self, question: str) -> str:
        if not self.llm:
            return "Error: OpenAI API Key not provided."
        
        try:
            response = self.llm.invoke(question)
            return response.content
        except Exception as e:
            return f"An error occurred: {str(e)}"
