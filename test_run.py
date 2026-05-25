import asyncio
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "backend"))
from backend.agents.orchestrator import SwarmOrchestrator
async def test_run():
    orc = SwarmOrchestrator()
    async def fake_update(update):
        print("UPDATE:", update)
    orc.set_update_callback(fake_update)
    print("Running swarm...")
    try:
        res = await orc.run_swarm("test")
        print("RESULT:", res)
    except Exception as e:
        import traceback
        traceback.print_exc()
asyncio.run(test_run())
