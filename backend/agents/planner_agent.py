from typing import Dict
from .base_agent import call_gemini

class PlannerAgent:
    def __init__(self, memory_store, message_bus):
        self.name = "PlannerAgent"
        self.memory = memory_store
        self.bus = message_bus
    
    async def create_plan(self, user_request: str) -> Dict:
        self.memory.update_agent_status(self.name, "🧠 Planning...")
        
        prompt = f"""
You are the Planner Agent in an AI agent swarm.
Your job is to break down the user's request into a clear execution plan.
User Request: {user_request}

Respond ONLY with a JSON object with this structure:
{{
    "project_name": "short name for the project",
    "tech_stack": ["list", "of", "technologies"],
    "tasks": [
        {{
            "id": "task_1",
            "agent": "CoderAgent",
            "title": "Task title",
            "description": "Detailed description",
            "priority": 1
        }}
    ],
    "architecture": "Brief description of the architecture"
}}
"""
        plan = await call_gemini(prompt)
        
        self.memory.store_agent_output(self.name, plan)
        self.memory.project_context["plan"] = plan
        self.memory.update_agent_status(self.name, "✅ Plan Ready")
        return plan
