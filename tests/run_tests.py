
from agents.coordinator import CoordinatorAgent

system = CoordinatorAgent()

queries = [
    "neural networks",
    "analyze transformers",
    "what did we discuss transformers"
]

for q in queries:
    print("\nQuery:", q)
    print("Response:", system.handle_query(q))
