from datetime import datetime

class ResearchAgent:
    def __init__(self):
        self.knowledge_base = {
            "neural networks": [
                "CNN – used for image processing",
                "RNN – used for sequential data",
                "Transformers – attention-based models"
            ],
            "transformers": [
                "Use self-attention mechanism",
                "Highly parallelizable",
                "Computationally expensive"
            ],
            "reinforcement learning": [
                "Agent-environment interaction",
                "Reward-based learning",
                "Exploration vs exploitation challenge"
            ]
        }

    def research(self, topic):
        print(f"[ResearchAgent] Researching topic: {topic}")
        data = self.knowledge_base.get(topic.lower(), ["No data found"])
        return {
            "topic": topic,
            "results": data,
            "confidence": 0.8,
            "timestamp": str(datetime.now())
        }
