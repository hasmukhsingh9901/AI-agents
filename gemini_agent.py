import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

print("Gemini AI agent is running! Type 'exit' to stop.")
def run_agent():
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Goodbye! 👋")
        return

    response = model.generate_content(user_input)
    print("Agent:", response.text)
        
        
if __name__ == "__main__":
    while True:
        run_agent()
        if not run_agent():
            break
        print()
    print("Exiting the agent...")  # Added exit message