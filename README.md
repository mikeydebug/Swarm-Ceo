<div align="center">

# 🐝 SWARM CEO
**The Distributed AI Agent Orchestration Platform**

[![Live Demo](https://img.shields.io/badge/Launch-Live_Demo-success?style=for-the-badge&logo=vercel)](https://swarm-ceo.vercel.app/)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)]()
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)]()

*Stop writing prompts. Start managing a virtual software engineering team.*

</div>

---

## 💡 The Vision (Why I built this)

Let's be honest: the market is flooded with basic AI wrappers that just take a prompt and spit out a massive, buggy text block. When I was brainstorming for this hackathon, I wanted to build something that actually mirrors **how real software engineering teams work.**

Real teams don't just write code immediately. We research dependencies, plan the architecture, write the code, run a security audit, and finally do a code review. **Swarm CEO** mimics this exact enterprise pipeline. You type one sentence, and the system spins up 6 isolated AI agents that communicate over a custom shared memory bus to build your project from scratch.

## 🚀 The 6-Agent Ecosystem

Unlike standard chatbots, Swarm CEO distributes the workload. Each agent has a strict, specialized system prompt and role:

| Agent | Role in the Swarm | Responsibility |
| :--- | :--- | :--- |
| **👨‍💼 Manager** | Orchestrator | Parses your initial request and defines the project scope. |
| **🌐 Researcher** | Tech Lead | Scans the requirements to determine the optimal, modern tech stack. |
| **🧠 Planner** | Architect | Generates a strict JSON blueprint and breaks the project into tasks. |
| **💻 Coder** | Executor | Reads the blueprint and writes production-ready code. |
| **🛡️ Security** | Auditor | Scans the generated codebase specifically for vulnerabilities. |
| **🔍 Reviewer** | QA | Performs the final code review and assigns a quality score. |

## ✨ Technical Highlights

* **Neural Swarm Visualizer:** I didn't want a boring terminal UI. I built a custom React visualization engine that tracks the agents in real-time. As agents execute tasks asynchronously, you see glowing data streams connecting them to the CEO node.
* **True WebSocket Streaming:** No dirty long-polling. The FastAPI backend streams execution logs directly to the frontend terminal via WebSockets, ensuring zero latency during the execution pipeline.
* **Shared Memory Bus:** Agents are completely stateless. I engineered a `SharedMemory` core that acts as a Redis-like state manager, allowing agents to pass complex JSON artifacts (like architectural plans) down the chain without losing context.
* **Rate-Limit Resilience:** Running 6 consecutive LLM calls usually breaks free-tier APIs. I implemented dynamic delays and explicitly connected to `gemini-1.5-flash` to handle the massive context windows required for passing code between agents.

## 💻 Local Setup

Want to run the Swarm locally? You'll need Node.js and Python.

### 1. Clone & API Key
```bash
git clone https://github.com/your-username/swarm-ceo.git
cd swarm-ceo
```
Create a `.env` file inside the `backend` folder and add your Google Gemini API Key:
```env
GEMINI_API_KEY=your_api_key_here
```

### 2. The Docker Way (Recommended)
This project is fully containerized for enterprise deployment.
```bash
docker-compose up -d --build
```
*Frontend will run on port 5173, backend on 8000.*

### 3. The Manual Way
**Backend (FastAPI):**
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```
**Frontend (React/Vite):**
```bash
cd frontend
npm install
npm run dev
```

## 🧠 Hackathon Learnings
The hardest part of this build wasn't the AI—it was the state management. Ensuring the WebSocket connection didn't drop while the backend waited for 6 sequential LLM responses required a lot of trial and error with Python's `asyncio` and custom error-handling loops. Seeing the laser animations sync up perfectly with the backend execution for the first time was easily the best moment of the hackathon!
