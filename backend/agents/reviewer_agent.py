from typing import Dict
from .base_agent import call_gemini

class ReviewerAgent:
    def __init__(self, memory_store, message_bus):
        self.name = "ReviewerAgent"
        self.memory = memory_store
        self.bus = message_bus
    
    async def review_all_code(self) -> Dict:
        self.memory.update_agent_status(self.name, "🔍 Reviewing Code...")
        artifacts = self.memory.get_all_artifacts()
        
        prompt = f"""
You are a Senior Software Engineer doing a code review.
Code to review: {str(artifacts)}

Respond ONLY with a JSON object:
{{
    "overall_score": 9.5,
    "overall_assessment": "Brief assessment",
    "positive_aspects": ["list"],
    "suggestions": ["list"]
}}
"""
        review = await call_gemini(prompt)
        self.memory.store_agent_output(self.name, review)
        self.memory.update_agent_status(self.name, "✅ Review Complete")
        return review
