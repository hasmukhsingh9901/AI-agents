# from agents import DebuggerAgent, TestAgent, DocumentationAgent
from agents.debugger_agent import DebuggerAgent
from agents.test_agent import TestAgent
from agents.doc_agent import DocumentationAgent
from agents.prompt_agent import PromptAgent

def show_menu():
    print("\n🤖 Welcome to DevAssist.AI")
    print("Choose an agent or press Enter to use general assistant:")
    print("1. Debugger")
    print("2. Test Generator")
    print("3. Documentation Generator")
    print("Press Enter to ask anything!")

def main():
    while True:
        show_menu()
        choice = input("\nEnter choice (1/2/3 or Enter): ").strip()
        user_input = input("\n📝 Your query or code:\n")

        if choice == "1":
            agent = DebuggerAgent()
        elif choice == "2":
            agent = TestAgent()
        elif choice == "3":
            agent = DocumentationAgent()
        else:
            agent = PromptAgent()  # General purpose assistant

        print("\n🧠 AI is working...\n")
        result = agent.run(user_input)
        print("📄 Result:\n")
        print(result)

        # Ask if user wants to continue
        cont = input("\n🔁 Do you want to ask something else? (y/n): ").strip().lower()
        if cont != "y":
            print("\n👋 Goodbye! Have a great day.")
            break

if __name__ == "__main__":
    main()
