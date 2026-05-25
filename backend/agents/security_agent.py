from typing import Dict
from .base_agent import call_gemini

class SecurityAgent:
    def __init__(self, memory_store, message_bus):
        self.name = "SecurityAgent"
        self.memory = memory_store
        self.bus = message_bus
    
    async def scan_code(self) -> Dict:
        self.memory.update_agent_status(self.name, "Scanning")
        
        artifacts = self.memory.get_all_artifacts()
        
        system_prompt = f"""
You are the SecurityAgent, the validator of the AI Swarm.
Scan the following generated code for vulnerabilities, bugs, or missing best practices.
Code to scan: {artifacts}

Respond ONLY with a JSON object:
{{
    "vulnerabilities_found": 0,
    "security_score": "10/10",
    "improvements": ["...", "..."]
}}
"""
        result = await call_gemini(system_prompt)
        
        self.memory.store_agent_output(self.name, result)
        self.memory.update_agent_status(self.name, "✅ Secured")
        return result
