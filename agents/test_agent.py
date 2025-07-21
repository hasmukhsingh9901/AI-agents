from core.agent_base import AgentBase
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

class TestAgent(AgentBase):
    def __init__(self, context=None):
        super().__init__(context)
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel("gemini-pro")

    def run(self, code_snippet):
        prompt = f"""
        You're an expert in writing unit tests. Write Python unit tests for the following code using best practices (e.g., pytest or unittest):

        Code:
        {code_snippet}
        """
        response = self.model.generate_content(prompt)
        return response.text
