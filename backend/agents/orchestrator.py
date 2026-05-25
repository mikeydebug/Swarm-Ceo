import asyncio
from typing import Dict, Callable
import uuid
from datetime import datetime

from .manager_agent import ManagerAgent
from .research_agent import ResearchAgent
from .planner_agent import PlannerAgent
from .coder_agent import CoderAgent
from .security_agent import SecurityAgent
from .reviewer_agent import ReviewerAgent
from core.memory_store import SharedMemory
from core.message_bus import MessageBus, Message

class SwarmOrchestrator:
    def __init__(self):
        self.memory = SharedMemory()
        self.bus = MessageBus()
        self.manager = ManagerAgent(self.memory, self.bus)
        self.researcher = ResearchAgent(self.memory, self.bus)
        self.planner = PlannerAgent(self.memory, self.bus)
        self.coder = CoderAgent(self.memory, self.bus)
        self.security = SecurityAgent(self.memory, self.bus)
        self.reviewer = ReviewerAgent(self.memory, self.bus)
        
        self.update_callback = None
        self.session_id = str(uuid.uuid4())
        
    def set_update_callback(self, callback: Callable):
        self.update_callback = callback
            
    async def broadcast_update(self, event_type: str, data: Dict):
        update = {
            "type": event_type,
            "data": data,
            "timestamp": datetime.now().isoformat(),
            "agent_statuses": self.memory.swarm_status
        }
        if self.update_callback:
            await self.update_callback(update)
            
    async def run_swarm(self, prompt: str) -> Dict:
        try:
            self.memory.project_context["goal"] = prompt
            await self.broadcast_update("swarm_start", {"message": "🚀 Swarm CEO initializing 6-agent ecosystem..."})
            
            # Phase 1: Management
            await self.broadcast_update("phase_start", {"phase": "Management", "message": "👨‍💼 ManagerAgent delegating..."})
            await asyncio.sleep(4)
            management = await self.manager.delegate_task(prompt)
            await self.broadcast_update("task_complete", {"task": "Management", "message": "✅ Delegation complete"})
            
            # Phase 2: Research
            await self.broadcast_update("phase_start", {"phase": "Research", "message": "🌐 ResearchAgent retrieving context..."})
            await asyncio.sleep(4)
            research = await self.researcher.research_topic(prompt)
            await self.broadcast_update("task_complete", {"task": "Research", "message": "✅ Research complete"})
            
            # Phase 3: Planning
            await self.broadcast_update("phase_start", {"phase": "Planning", "message": "🧠 PlannerAgent architecting..."})
            await asyncio.sleep(4)
            plan = await self.planner.create_plan(prompt)
            await self.broadcast_update("task_complete", {"task": "Planning", "message": "✅ Plan ready"})
            
            # Phase 4: Coding
            await self.broadcast_update("phase_start", {"phase": "Coding", "message": "💻 CoderAgent executing tasks..."})
            tasks = plan.get("tasks", [])
            for task in tasks:
                if task.get("agent") == "CoderAgent":
                    await self.broadcast_update("task_start", {"task": task["title"], "message": f"Writing: {task['title']}"})
                    await asyncio.sleep(4)
                    await self.coder.execute_task(task)
                    await self.broadcast_update("task_complete", {
                        "task": task["title"],
                        "message": f"✅ {task['title']} complete",
                        "artifacts": self.memory.get_all_artifacts()
                    })
            
            # Phase 5: Security
            await self.broadcast_update("phase_start", {"phase": "Security", "message": "🛡️ SecurityAgent scanning..."})
            await asyncio.sleep(4)
            security = await self.security.scan_code()
            await self.broadcast_update("task_complete", {"task": "Security", "message": "✅ Security scan complete"})
            
            # Phase 6: Review
            await self.broadcast_update("phase_start", {"phase": "Review", "message": "🔍 ReviewerAgent validating..."})
            await asyncio.sleep(4)
            review = await self.reviewer.review_all_code()
            score = review.get('overall_score', 'N/A')
            await self.broadcast_update("task_complete", {"task": "Review", "message": f"✅ Code score: {score}"})
            
            final_result = {
                "status": "success",
                "management": management,
                "research": research,
                "plan": plan,
                "security": security,
                "review": review,
                "artifacts": self.memory.get_all_artifacts(),
                "summary": {
                    "total_files": len(self.memory.artifacts)
                }
            }
            
            await self.broadcast_update("swarm_complete", {
                "message": "🎉 Swarm execution complete!",
                "summary": final_result["summary"]
            })
            
            return final_result
            
        except Exception as e:
            await self.broadcast_update("error", {"message": f"❌ Swarm failed: {str(e)}"})
            return {"status": "error", "message": str(e)}
