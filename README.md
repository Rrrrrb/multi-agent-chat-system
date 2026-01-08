# Multi-Agent AI System with Memory & Analysis

A modular **multi-agent architecture** in Python that demonstrates how intelligent agents can **research, analyze, coordinate, and retain memory** across interactions.  
This project showcases foundational concepts behind **agentic AI systems**, including semantic memory retrieval and task delegation.

---

## Project Overview

The system is orchestrated by a **Coordinator** agent that routes user queries to specialized agents:

- **ResearchAgent** – Gathers knowledge from a predefined knowledge base  
- **AnalysisAgent** – Performs structured analysis on research results  
- **MemoryAgent** – Stores and retrieves information using vector similarity  
- **VectorStore** – Enables semantic search with TF-IDF and cosine similarity  

The architecture supports:
- Simple factual queries  
- Analysis and comparison requests  
- Multi-step reasoning  
- Memory-based follow-up questions (e.g., *“discuss earlier topic”*)

---

## Project Structure

.
├── agents/
│ ├── pycache/
│ ├── analysis_agent.py
│ ├── coordinator.py
│ ├── memory_agent.py
│ ├── research_agent.py
│
├── memory/
│ ├── pycache/
│ └── vector_store.py
│
├── outputs/
│ ├── simple_query.txt
│ ├── multi_step.txt
│ ├── complex_query.txt
│ ├── collaborative.txt
│ └── memory_test.txt
│
└── README.md



---

## Agent Responsibilities

### ResearchAgent (`agents/research_agent.py`)
- Maintains an internal domain-specific knowledge base  
- Retrieves relevant information based on the query topic  
- Returns structured results with confidence score and timestamp  

**Example Topics Supported**
- Neural Networks  
- Transformers  
- Reinforcement Learning  

---

###  AnalysisAgent (`agents/analysis_agent.py`)
- Consumes research outputs  
- Produces structured analytical insights  
- Adds confidence score and timestamp  

---

### MemoryAgent (`agents/memory_agent.py`)
- Stores both research and analysis outputs  
- Retrieves relevant past information using semantic similarity  
- Maintains an in-memory interaction history  

---

### VectorStore (`memory/vector_store.py`)
- Implements semantic similarity search  
- Built using:
  - `TfidfVectorizer`
  - `cosine_similarity`
- Matches user queries against stored memory records  

---

### Coordinator (`agents/coordinator.py`)
The central controller responsible for:
1. Receiving user queries  
2. Checking memory for prior relevant context  
3. Delegating tasks to the ResearchAgent  
4. Optionally invoking the AnalysisAgent  
5. Storing all outputs in memory  
6. Returning the most relevant response  

---

## System Workflow

User Query
   ↓
Coordinator
   ↓
MemoryAgent (retrieve if relevant)
   ↓
ResearchAgent
   ↓
MemoryAgent (store)
   ↓
AnalysisAgent (if requested)
   ↓
MemoryAgent (store)
   ↓
Response Returned to User

---
 
## Example Usage
from agents.coordinator import Coordinator

coordinator = Coordinator()

coordinator.handle_query("neural networks")
coordinator.handle_query("analyze transformers")
coordinator.handle_query("compare reinforcement learning")
coordinator.handle_query("discuss earlier topic")

---
 
## Output Format

Typical response structure:

{
  "topic": "Transformers",
  "results": [
    "Use self-attention mechanism",
    "Highly parallelizable",
    "Computationally expensive"
  ],
  "analysis": [
    "Analysis: Use self-attention mechanism",
    "Analysis: Highly parallelizable",
    "Analysis: Computationally expensive"
  ],
  "confidence": 0.75,
  "timestamp": "YYYY-MM-DD HH:MM:SS"
}

---
 
## Dependencies

Ensure the following dependency is installed:

pip install scikit-learn

---
 
## Key Features

- Modular and extensible agent-based design

- Semantic memory retrieval using vector similarity

- Clear separation of concerns between agents

- Easy to extend with new agents or knowledge domains

- Ideal for learning and experimenting with agentic AI systems

---
 
 ## Future Enhancements

- Persistent memory storage (database or embedding store)

- Integration with real-time web research

- LLM-powered reasoning and planning

- Advanced confidence scoring

- Multi-agent collaboration and negotiation

## License

This project is intended for educational and experimental use.
You are free to modify, extend, and build upon it.
