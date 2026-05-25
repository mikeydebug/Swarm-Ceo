from typing import Dict
from .base_agent import call_gemini, call_gemini_text

class CoderAgent:
    def __init__(self, memory_store, message_bus):
        self.name = "CoderAgent"
        self.memory = memory_store
        self.bus = message_bus
    
    async def execute_task(self, task: Dict) -> Dict:
        self.memory.update_agent_status(self.name, f"💻 Coding: {task['title']}")
        context = self.memory.get_context_summary()
        plan = self.memory.project_context.get("plan", {})
        
        prompt = f"""
You are an expert software engineer - CoderAgent.
Context: {context}
Tech Stack: {plan.get('tech_stack', [])}
Current Task: {task['title']} - {task['description']}

Write production-quality code. 
Respond ONLY with a JSON object with this structure:
{{
    "files": [
        {{
            "filename": "path/to/file.py",
            "content": "full file content here"
        }}
    ],
    "explanation": "What was built"
}}
"""
        result = await call_gemini(prompt)
        
        # Handle variations in JSON keys from the LLM
        files = result.get("files") or result.get("file") or result.get("code_files") or []
        if isinstance(files, dict):
            files = [files]
            
        for file_info in files:
            filename = file_info.get("filename") or file_info.get("name") or file_info.get("path") or f"file_{len(self.memory.artifacts)}.txt"
            content = file_info.get("content") or file_info.get("code") or ""
            if content:
                self.memory.store_artifact(filename, content)
            
        self.memory.store_agent_output(self.name, result)
        self.memory.update_agent_status(self.name, "✅ Code Ready")
        return result
