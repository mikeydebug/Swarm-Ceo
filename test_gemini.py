import asyncio
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from backend.agents.base_agent import call_gemini

async def test():
    print("Calling Gemini...")
    res = await call_gemini("Say hello in JSON { 'msg': 'hello' }")
    print("Result:", res)

asyncio.run(test())
