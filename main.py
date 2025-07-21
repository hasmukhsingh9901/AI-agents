from agents import DebuggerAgent, TestAgent, DocumentationAgent

def main():
    print("🤖 Welcome to DevAssist.AI")
    print("Choose an agent:")
    print("1. Debugger")
    print("2. Test Generator")
    print("3. Documentation Generator")

    choice = input("Enter choice: ")
    code_input = input("\nPaste your code:\n")

    if choice == "1":
        agent = DebuggerAgent()
    elif choice == "2":
        agent = TestAgent()
    elif choice == "3":
        agent = DocumentationAgent()
    else:
        print("Invalid choice.")
        return

    print("\n🧠 AI is working...\n")
    result = agent.run(code_input)
    print("📄 Result:\n")
    print(result)

if __name__ == "__main__":
    main()
