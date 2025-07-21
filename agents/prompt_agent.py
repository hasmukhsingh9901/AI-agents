from core.agent_base import AgentBase
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

class PromptAgent(AgentBase):
    def __init__(self, context=None):
        super().__init__(context)
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = genai.GenerativeModel("gemini-pro")

    def run(self, user_input):
        prompt = f"""
    You are PromptAgent, a brilliant, helpful, and friendly AI assistant trained to answer any type of question.

    Your goal is to:
    - Understand what the user is really asking
    - Respond with clear, accurate, and relevant information
    - Be friendly, respectful, and professional in tone
    - Help with real-world tasks like explaining concepts, solving problems, offering advice, or having thoughtful conversation

    User message:
    {user_input}
    """
        response = self.model.generate_content(prompt)
        return response.text

