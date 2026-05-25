# 🐝 Swarm CEO

![Live Demo](https://img.shields.io/badge/Live_Demo-Online-success?style=for-the-badge)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini_API-8E75B2?style=for-the-badge&logo=googlebard&logoColor=white)

**Live Demo:** [https://swarm-ceo.vercel.app/](https://swarm-ceo.vercel.app/)

Swarm CEO is a distributed AI agent orchestration platform. You give it a single prompt, and it spins up a virtual software agency—complete with 6 distinct "employees"—to research, plan, write, scan, and review your code entirely in the background.

## 💡 The Inspiration

We've all seen basic AI wrappers that just take a prompt and spit out a long text response. I wanted to build something that felt like a real engineering team. 

When you build software in the real world, you don't just write code immediately. You plan the architecture, research dependencies, write the code, run a security audit, and do a code review. Swarm CEO mimics this exact pipeline using isolated AI agents communicating over a shared memory bus.

## 🚀 Key Features

*   **The 6-Agent Pipeline:**
    *   **ManagerAgent:** Acts as the orchestrator. Breaks down the initial request into project scope.
    *   **ResearchAgent:** Scans the requirements and determines the optimal tech stack.
    *   **PlannerAgent:** Generates the JSON blueprint and task list.
    *   **CoderAgent:** Actually writes the code based on the strict architectural plan.
    *   **SecurityAgent:** Audits the generated codebase for vulnerabilities.
    *   **ReviewerAgent:** Performs final QA and assigns a code quality score.
*   **Neural Swarm Visualizer:** A custom-built React layout that tracks the agents in real-time. When an agent is working, a data stream physically connects it to the CEO node in the UI.
*   **Websocket Architecture:** No polling. The backend streams execution logs directly to the frontend terminal via WebSockets.

## 🏗️ Architecture Stack

*   **Frontend:** React, Vite, Framer Motion (for the animations), and Vanilla CSS (custom glassmorphism design system).
*   **Backend:** Python, FastAPI, Uvicorn, and WebSockets.
*   **AI Engine:** Google Gemini 1.5 Flash (chosen for its massive context window and high rate limits to support 6 consecutive agent calls).
*   **Deployment:** Vercel (Frontend) & Render (Backend).

## 💻 Local Setup Instructions

If you want to run this locally, you'll need Node.js and Python installed.

### 1. Clone the repo
```bash
git clone https://github.com/your-username/swarm-ceo.git
cd swarm-ceo
```

### 2. Set up the Backend
You need a free Gemini API key from Google AI Studio.
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```
Create a `.env` file inside the `backend` folder:
```env
GEMINI_API_KEY=your_api_key_here
```
Run the server:
```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Set up the Frontend
Open a new terminal window.
```bash
cd frontend
npm install
npm run dev
```
Open `http://localhost:5173` in your browser.

## 🐳 Docker Setup

For enterprise deployment, the entire stack is containerized.
```bash
# Make sure your .env file is present in the backend directory
docker-compose up -d --build
```

## 🧠 What I learned
Building the WebSocket connection was trickier than expected. Since the agents run sequentially and hit the LLM API heavily, I had to implement custom async sleeps and a centralized `SharedMemory` store so the agents could pass context (like the architectural plan) down the chain without breaking the frontend connection.
