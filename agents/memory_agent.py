
import datetime

class MemoryAgent:
    def __init__(self):
        self.knowledge_base = []
        self.conversation = []

    def store(self, topic, content, agent, confidence):
        self.knowledge_base.append({
            "time": datetime.datetime.now().isoformat(),
            "topic": topic,
            "content": content,
            "agent": agent,
            "confidence": confidence
        })

    def search(self, topic):
        return [k for k in self.knowledge_base if topic.lower() in k["topic"].lower()]

    def log_conversation(self, query, response):
        self.conversation.append({
            "query": query,
            "response": response
        })
