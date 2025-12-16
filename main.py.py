
from agents.coordinator import CoordinatorAgent

if __name__ == "__main__":
    system = CoordinatorAgent()
    print("Multi-Agent Chat System Running...")
    print(system.handle_query("neural networks"))
