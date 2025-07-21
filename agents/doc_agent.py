from core.agent_base import AgentBase
import google.generativeai as genai
import os

class DocumentationAgent(AgentBase):
    def __init__(self, context=None):
        super().__init__(context)
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel("gemini-pro")

    def run(self, code_snippet):
        prompt = f"""
        You're a documentation expert. Analyze the following code and generate clear docstrings and a Markdown-style summary.

        Code:
        {code_snippet}
        """
        response = self.model.generate_content(prompt)
        return response.text
