from core.agent_base import AgentBase
import google.generativeai as genai
import os

class DebuggerAgent(AgentBase):
    def __init__(self, context=None):
        super().__init__(context)
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel("gemini-pro")

    def run(self, code_snippet):
        prompt = f"""
        You're a senior software engineer. Given the following code snippet, find and fix any bugs.
        Explain your reasoning and suggest best practices.

        Code:
        {code_snippet}
        """
        response = self.model.generate_content(prompt)
        return response.text
