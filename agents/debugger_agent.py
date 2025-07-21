from core.agent_base import AgentBase
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file  
import os

class DebuggerAgent(AgentBase):
    def __init__(self, context=None):
        super().__init__(context)
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel("gemini-1.5-flash")
        
    def run(self, code_snippet):
        prompt = f"""
        You are a code debugger. Your task is to analyze the provided code snippet and identify any potential issues or bugs.
        The code snippet is:
        {code_snippet}
        Please provide a detailed analysis of the code, including any errors, potential improvements, and suggestions for debugging.
        :param code_snippet: The code snippet to analyze.
        :return: A detailed analysis of the code snippet.
        """
        response = self.model.generate_content(prompt)
        return response.text