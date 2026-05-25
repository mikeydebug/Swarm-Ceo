from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List
import asyncio
import json
import os
from dotenv import load_dotenv

load_dotenv()

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.orchestrator import SwarmOrchestrator

app = FastAPI(
    title="Swarm CEO API",
    description="AI Agent Swarm Orchestration Platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

active_connections: Dict[str, WebSocket] = {}

class TaskRequest(BaseModel):
    request: str
    session_id: str = None

@app.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    await websocket.accept()
    active_connections[session_id] = websocket
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        if session_id in active_connections:
            del active_connections[session_id]

@app.post("/api/run-swarm")
async def run_swarm(request: TaskRequest):
    orchestrator = SwarmOrchestrator()
    
    async def send_update(update: Dict):
        session_id = request.session_id
        if session_id and session_id in active_connections:
            try:
                await active_connections[session_id].send_json(update)
            except Exception as e:
                print(f"WebSocket send error: {e}")
                
    orchestrator.set_update_callback(send_update)
    result = await orchestrator.run_swarm(request.request)
    return result

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}
