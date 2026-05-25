from typing import Dict
from .base_agent import call_gemini

class ResearchAgent:
    def __init__(self, memory_store, message_bus):
        self.name = "ResearchAgent"
        self.memory = memory_store
        self.bus = message_bus
    
    async def research_topic(self, prompt: str) -> Dict:
        self.memory.update_agent_status(self.name, "Researching")
        
        system_prompt = f"""
You are the ResearchAgent, the retriever of the AI Swarm.
Analyze the request and return best practices and tech stack recommendations.
User Request: {prompt}

Respond ONLY with a JSON object:
{{
    "tech_stack_recommendations": ["...", "..."],
    "best_practices": ["...", "..."],
    "potential_pitfalls": ["...", "..."]
}}
"""
        result = await call_gemini(system_prompt)
        
        self.memory.store_agent_output(self.name, result)
        self.memory.update_agent_status(self.name, "✅ Research Complete")
        return result
