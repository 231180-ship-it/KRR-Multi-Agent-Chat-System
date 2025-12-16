
class ResearchAgent:
    def __init__(self):
        self.knowledge = {
            "neural networks": "Neural networks include CNNs, RNNs, and Transformers.",
            "transformers": "Transformers rely on self-attention and parallel computation.",
            "reinforcement learning": "RL uses rewards to learn optimal behavior."
        }

    def research(self, topic):
        print("[ResearchAgent] Searching...")
        return self.knowledge.get(topic.lower(), "No data found.")
