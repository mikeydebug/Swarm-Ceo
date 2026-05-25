import asyncio
import os
import sys
from dotenv import load_dotenv

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "backend"))
load_dotenv('backend/.env')

from core.message_bus import MessageBus
from core.memory_store import SharedMemory
from agents.planner_agent import PlannerAgent
from agents.coder_agent import CoderAgent
from agents.reviewer_agent import ReviewerAgent
from agents.orchestrator import SwarmOrchestrator

async def test_swarm():
    orc = SwarmOrchestrator()
    print("Running swarm...")
    res = await orc.run_swarm("create a simple html file")
    print("Result:")
    print(res)

asyncio.run(test_swarm())
