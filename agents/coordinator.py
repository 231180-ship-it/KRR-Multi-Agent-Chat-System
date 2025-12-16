
from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.memory_agent import MemoryAgent

class CoordinatorAgent:
    def __init__(self):
        self.memory = MemoryAgent()
        self.research_agent = ResearchAgent()
        self.analysis_agent = AnalysisAgent()

    def handle_query(self, user_query):
        print("[Coordinator] Query:", user_query)

        if "analyze" in user_query.lower():
            topic = user_query.split()[-1]
            research = self.research_agent.research(topic)
            analysis = self.analysis_agent.analyze(research)
            answer = research + " " + analysis
            self.memory.store(topic, answer, "Coordinator", 0.9)

        elif "what did we discuss" in user_query.lower():
            topic = user_query.split()[-1]
            past = self.memory.search(topic)
            answer = past[-1]["content"] if past else "No memory found."

        else:
            answer = self.research_agent.research(user_query)
            self.memory.store(user_query, answer, "ResearchAgent", 0.7)

        self.memory.log_conversation(user_query, answer)
        return answer
