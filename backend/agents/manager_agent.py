from typing import Dict
from .base_agent import call_gemini

class ManagerAgent:
    def __init__(self, memory_store, message_bus):
        self.name = "ManagerAgent"
        self.memory = memory_store
        self.bus = message_bus
    
    async def delegate_task(self, prompt: str) -> Dict:
        self.memory.update_agent_status(self.name, "Processing")
        
        system_prompt = f"""
You are the ManagerAgent, the leader of a distributed AI Swarm.
Your job is to analyze the user's request and delegate it to the team.
User Request: {prompt}

Respond ONLY with a JSON object detailing the scope:
{{
    "project_name": "...",
    "complexity": "High/Medium/Low",
    "delegation_strategy": "..."
}}
"""
        result = await call_gemini(system_prompt)
        
        self.memory.store_agent_output(self.name, result)
        self.memory.update_agent_status(self.name, "✅ Delegated")
        return result
