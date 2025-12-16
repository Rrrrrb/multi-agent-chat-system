from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.memory_agent import MemoryAgent

class Coordinator:
    def __init__(self):
        self.research_agent = ResearchAgent()
        self.analysis_agent = AnalysisAgent()
        self.memory_agent = MemoryAgent()

    def handle_query(self, query):
        print(f"\n[Coordinator] User query: {query}")

        # Memory check
        if "earlier" in query or "discuss" in query:
            memory = self.memory_agent.retrieve(query)
            if memory:
                return memory
            else:
                return {"message": "No prior information found in memory."}

        # Research
        research_output = self.research_agent.research(query)
        self.memory_agent.store(research_output)

        # Analysis if needed
        if "analyze" in query or "compare" in query:
            analysis_output = self.analysis_agent.analyze(research_output)
            self.memory_agent.store(analysis_output)
            return analysis_output

        return research_output
