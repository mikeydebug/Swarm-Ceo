import asyncio
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "backend"))
from backend.core.memory_store import SharedMemory
from backend.core.message_bus import MessageBus
from backend.agents.coder_agent import CoderAgent

async def run():
    mem = SharedMemory()
    bus = MessageBus()
    coder = CoderAgent(mem, bus)
    
    task = {"title": "Create C program with if-else conditions", "description": "Write a basic C program demonstrating if-else statements"}
    res = await coder.execute_task(task)
    print("RESULT FROM LLM:", res)
    print("ARTIFACTS:", mem.get_all_artifacts())

asyncio.run(run())
