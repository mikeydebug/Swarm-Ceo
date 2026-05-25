from typing import Dict, List, Any, Optional
from datetime import datetime

class SharedMemory:
    """Shared memory store for all agents."""
    
    def __init__(self):
        self.project_context: Dict = {}
        self.agent_outputs: Dict[str, List] = {}
        self.task_queue: List[Dict] = []
        self.completed_tasks: List[Dict] = []
        self.artifacts: Dict[str, str] = {}
        self.conversation_history: List[Dict] = []
        self.swarm_status: Dict[str, str] = {}
    
    def set_project(self, project_id: str, description: str):
        self.project_context = {
            "id": project_id,
            "description": description,
            "created_at": datetime.now().isoformat(),
            "status": "initializing"
        }
    
    def store_agent_output(self, agent_name: str, output: Any):
        if agent_name not in self.agent_outputs:
            self.agent_outputs[agent_name] = []
        self.agent_outputs[agent_name].append({
            "output": output,
            "timestamp": datetime.now().isoformat()
        })
    
    def store_artifact(self, filename: str, content: str):
        self.artifacts[filename] = content
    
    def get_artifact(self, filename: str) -> Optional[str]:
        return self.artifacts.get(filename)
    
    def update_agent_status(self, agent_name: str, status: str):
        self.swarm_status[agent_name] = status
    
    def get_all_artifacts(self) -> Dict[str, str]:
        return self.artifacts
    
    def get_context_summary(self) -> str:
        return f"""
Project: {self.project_context.get('description', 'Unknown')}
Status: {self.project_context.get('status', 'Unknown')}
Completed Tasks: {len(self.completed_tasks)}
Pending Tasks: {len(self.task_queue)}
Artifacts Created: {list(self.artifacts.keys())}
Agent Outputs Available: {list(self.agent_outputs.keys())}
        """.strip()
