from agents.debugger_agent import DebuggerAgent

def main():
    print("👨‍💻 DevAssist AI CLI")
    print("Choose an agent:")
    print("1. Debugger")

    choice = input("Enter choice: ")

    if choice == "1":
        code = input("Paste your code: ")
        agent = DebuggerAgent()
        output = agent.run(code)
        print("\n💡 Suggestion:\n", output)
