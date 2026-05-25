<div align="center">

# 🐝 Swarm CEO
**The Distributed AI Agent Orchestration Platform**

[![Live Demo](https://img.shields.io/badge/Launch-Live_Demo-success?style=for-the-badge&logo=vercel)](https://swarm-ceo.vercel.app/)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)]()
[![Gemini](https://img.shields.io/badge/Gemini_API-8E75B2?style=for-the-badge&logo=googlebard&logoColor=white)]()
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)]()

*Stop writing prompts. Start managing a virtual software engineering team.*

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Project Goals](#-project-goals)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [System Architecture](#-system-architecture)
- [The 6-Agent Ecosystem](#-the-6-agent-ecosystem)
- [Installation & Setup](#-installation)
- [Environment Configuration](#-configuration)
- [Project Structure](#-project-structure)
- [API Endpoints & WebSockets](#-api-endpoints)
- [Future Enhancements](#-future-enhancements)
- [License](#-license)

---

## 🌟 Overview

Swarm CEO is a full-stack, distributed AI orchestration platform. Unlike traditional chatbots that use a single LLM call to generate text, Swarm CEO mimics a real-world enterprise engineering team. You provide a single objective, and the platform spins up 6 distinct AI agents that communicate over a custom shared memory bus to research, architect, code, audit, and review the software entirely in the background.

## 🎯 Project Goals

* Move beyond simple "AI wrappers" by implementing a true distributed agent architecture.
* Achieve zero-latency execution tracking via direct WebSocket streaming.
* Create a visually stunning, neural-network-style frontend to visualize asynchronous tasks.
* Implement a robust `SharedMemory` system to pass architectural blueprints safely between stateless agents.
* Overcome severe LLM rate limits using dynamic execution delays and context management.

## ✨ Key Features

### 🧠 Distributed AI Workload
* Sequential 6-Agent execution pipeline.
* Role-based prompting (Manager, Tech Lead, Architect, Coder, Auditor, QA).
* Artifact generation (code files) stored in virtual shared memory.

### ⚡ Real-Time Telemetry
* True WebSocket streaming (No long-polling!).
* Live terminal output logging every agent's thought process.
* Custom Neural Swarm Visualizer built with React and CSS animations.

### 🛡️ Enterprise Architecture
* Containerized with Docker and Docker Compose.
* Decoupled FastAPI backend and React frontend.
* Custom Message Bus for inter-agent event handling.

---

## 🛠️ Tech Stack

### Backend
| Technology | Purpose |
| :--- | :--- |
| **Python 3.10+** | Core runtime environment |
| **FastAPI** | High-performance async web framework |
| **Uvicorn** | ASGI server for Python |
| **WebSockets** | Real-time bi-directional streaming |
| **Google Gemini 1.5 Flash** | AI Engine (Chosen for massive 1,500 req/day rate limit and massive context window) |

### Frontend
| Technology | Purpose |
| :--- | :--- |
| **React 18** | UI Component library |
| **Vite** | Blazing fast build tool |
| **Vanilla CSS** | Custom glassmorphism design system |
| **Lucide React** | Premium icon library |

---

## 🏗️ System Architecture

```text
┌─────────────────────────────────────────────────────────────┐
│                      Client Browser (React)                 │
│      [Neural Visualizer]  [Terminal]  [Artifact Viewer]     │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ HTTP POST /api/run-swarm
                         │ WebSocket ws://.../ws/{session}
                         │
┌────────────────────────▼────────────────────────────────────┐
│                      FastAPI Backend                        │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │               Swarm Orchestrator                      │  │
│  └─┬──────────────────────┬────────────────────────────┬─┘  │
│    │                      │                            │    │
│    ▼                      ▼                            ▼    │
│ ┌──────────┐         ┌──────────┐                 ┌─────────┐│
│ │ Message  │ ◄──────►│ Shared   │ ◄──────────────►│ Agents  ││
│ │ Bus      │         │ Memory   │                 │ (1 to 6)││
│ └──────────┘         └──────────┘                 └────┬────┘│
└────────────────────────────────────────────────────────│────┘
                                                         │
                                                  REST API Call
                                                         │
┌────────────────────────────────────────────────────────▼────┐
│                    Google Gemini 1.5 API                    │
└─────────────────────────────────────────────────────────────┘
```

---

## 🤖 The 6-Agent Ecosystem

| Agent | Role | Responsibility |
| :--- | :--- | :--- |
| **👨‍💼 Manager** | Orchestrator | Parses the initial request, sets the goal, and defines the strict project scope. |
| **🌐 Researcher** | Tech Lead | Retrieves context and determines the optimal, modern tech stack required. |
| **🧠 Planner** | Architect | Generates a strict JSON blueprint and breaks the project into executable tasks. |
| **💻 Coder** | Executor | Reads the blueprint from Shared Memory and writes production-ready code. |
| **🛡️ Security** | Auditor | Scans the generated codebase explicitly looking for vulnerabilities and edge cases. |
| **🔍 Reviewer** | QA | Performs the final code review and assigns an enterprise quality score. |

---

## 🚀 Installation

### Prerequisites
* Node.js (v18+)
* Python (v3.9+)
* Docker (Optional, for containerized deployment)
* Google Gemini API Key

### Option A: Docker Setup (Recommended)
The absolute easiest way to run the full stack:
```bash
git clone https://github.com/mikeydebug/swarm-ceo.git
cd swarm-ceo
# Add your GEMINI_API_KEY to backend/.env
docker-compose up -d --build
```
*Frontend runs on `http://localhost:5173` | Backend runs on `http://localhost:8000`*

### Option B: Manual Setup

**1. Backend**
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

**2. Frontend**
Open a new terminal:
```bash
cd frontend
npm install
npm run dev
```

---

## ⚙️ Configuration

Create a `.env` file in the `backend` directory:
```env
# Required: Your Google Gemini API Key
GEMINI_API_KEY=your_api_key_here
```

Create a `.env` file in the `frontend` directory (For deployment only):
```env
# Point this to your hosted backend (e.g., Render)
VITE_BACKEND_URL=your-backend-url.onrender.com
```

---

## 📁 Project Structure

```text
swarm-ceo/
│
├── backend/                        # FastAPI Python Backend
│   ├── api/
│   │   └── main.py                 # REST & WebSocket endpoints
│   ├── agents/
│   │   ├── orchestrator.py         # Manages the 6-agent lifecycle
│   │   ├── base_agent.py           # Gemini LLM integration logic
│   │   ├── manager_agent.py        
│   │   ├── research_agent.py       
│   │   ├── planner_agent.py        
│   │   ├── coder_agent.py          # Generates code artifacts
│   │   ├── security_agent.py       
│   │   └── reviewer_agent.py       
│   ├── core/
│   │   ├── memory_store.py         # Virtual shared memory (JSON state)
│   │   └── message_bus.py          # Event-driven pub/sub system
│   └── requirements.txt            # Python dependencies
│
├── frontend/                       # React + Vite Frontend
│   ├── src/
│   │   ├── components/
│   │   │   ├── SwarmVisualizer.jsx # Neural node UI component
│   │   │   ├── Terminal.jsx        # Live logging component
│   │   │   └── ArtifactViewer.jsx  # Syntax-highlighted code viewer
│   │   ├── App.jsx                 # Main layout and WebSocket logic
│   │   ├── App.css                 # Glassmorphism structural styles
│   │   └── index.css               # Design tokens & animations
│   └── package.json
│
├── docker-compose.yml              # Multi-container orchestration
└── README.md                       
```

---

## 🌐 API Endpoints

### REST API
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/api/health` | Health check for deployment monitoring |
| **POST** | `/api/run-swarm` | Initiates the 6-agent pipeline. Requires `{ request: "string", session_id: "uuid" }` |

### WebSockets
| Protocol | Endpoint | Description |
| :--- | :--- | :--- |
| **WS** | `/ws/{session_id}` | Streams real-time JSON execution logs. Valid events: `swarm_start`, `phase_start`, `task_complete`, `error`, `swarm_complete` |

---

## 🔮 Future Enhancements

* **Agent Chat Interface:** Allow users to interrupt the PlannerAgent to manually approve architectural decisions before coding begins.
* **Persistent Database:** Replace the in-memory `SharedMemory` store with PostgreSQL to save historical projects and codebases.
* **Multi-File Context Limits:** Implement RAG (Retrieval-Augmented Generation) to allow the CoderAgent to build massive repositories without hitting token limits.

---

## 👨‍💻 Author

**Mayank Soni**
* GitHub: [@mikeydebug](https://github.com/mikeydebug)

---
<div align="center">
Made with ❤️ for the Hackathon. 
</div>
