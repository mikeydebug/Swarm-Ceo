import React, { useState, useEffect, useRef } from 'react';
import { Play } from 'lucide-react';
import SwarmVisualizer from './components/SwarmVisualizer';
import LiveTerminal from './components/LiveTerminal';
import ArtifactViewer from './components/ArtifactViewer';
import './App.css';

export default function App() {
  const [sessionId] = useState(() => `session_${Date.now()}`);
  const [isRunning, setIsRunning] = useState(false);
  const [request, setRequest] = useState('');
  const [agentStatuses, setAgentStatuses] = useState({});
  const [executionLog, setExecutionLog] = useState([]);
  const [currentPhase, setCurrentPhase] = useState('');
  const [artifacts, setArtifacts] = useState({});
  const wsRef = useRef(null);

  useEffect(() => {
    const backendUrl = import.meta.env.VITE_BACKEND_URL || 'localhost:8000';
    const wsProtocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    
    // If VITE_BACKEND_URL includes http/https, strip it for the websocket
    const wsHost = backendUrl.replace(/^https?:\/\//, '');
    const ws = new WebSocket(`${wsProtocol}//${wsHost}/ws/${sessionId}`);
    
    wsRef.current = ws;
    
    ws.onmessage = (event) => {
      try {
        const update = JSON.parse(event.data);
        if (update.agent_statuses) setAgentStatuses(update.agent_statuses);
        
        setExecutionLog(prev => [...prev, update]);
        if (update.type === 'task_complete' && update.data.artifacts) {
          setArtifacts(update.data.artifacts);
        }
        if (update.type === 'phase_start') setCurrentPhase(update.data.phase);
        if (update.type === 'swarm_complete') {
          setIsRunning(false);
          setCurrentPhase('Complete');
        }
        if (update.type === 'error') {
          setIsRunning(false);
          setCurrentPhase('Error');
        }
        if (update.type === 'error') {
          setIsRunning(false);
          setCurrentPhase('Error');
        }
      } catch (e) {
        console.error("WS parsing error", e);
      }
    };
    
    return () => ws.close();
  }, [sessionId]);

  const handleRun = async () => {
    if (!request.trim()) return;
    setIsRunning(true);
    setExecutionLog([]);
    setCurrentPhase('Initializing');
    setAgentStatuses({});
    setArtifacts({});
    
    try {
      const backendUrl = import.meta.env.VITE_BACKEND_URL || 'http://localhost:8000';
      const apiUrl = backendUrl.startsWith('http') ? backendUrl : `http://${backendUrl}`;
      
      const response = await fetch(`${apiUrl}/api/run-swarm`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ request, session_id: sessionId })
      });
      const data = await response.json();
      if (data.artifacts) {
        setArtifacts(data.artifacts);
      }
    } catch (error) {
      console.error('Error running swarm:', error);
      setIsRunning(false);
    }
  };

  return (
    <div className="app-container">
      <header className="header glass-panel">
        <div className="header-brand">
          <div className="header-icon">🐝</div>
          <div className="header-title">
            <h1 className="gradient-text">SWARM CEO</h1>
            <p>AI Agent Swarm Orchestration Platform</p>
          </div>
        </div>
      </header>

      <main className="main-content">
        <div className="left-sidebar">
          <div className="input-section glass-panel">
            <textarea 
              className="task-input"
              placeholder="Describe the software you want to build... (e.g., 'Build a fast python API for a todo list')"
              value={request}
              onChange={(e) => setRequest(e.target.value)}
              rows={4}
            />
            <button 
              className="run-btn" 
              onClick={handleRun}
              disabled={isRunning || !request.trim()}
            >
              <Play size={18} />
              {isRunning ? 'Swarm Active...' : 'Launch Swarm'}
            </button>
          </div>

          <div className="terminal-wrapper">
            <LiveTerminal logs={executionLog} />
          </div>
        </div>

        <div className="right-content">
          <div className="visualization-area glass-panel">
            <SwarmVisualizer 
              currentPhase={currentPhase} 
              agentStatuses={agentStatuses} 
            />
          </div>
          <div className="artifacts-wrapper">
            <ArtifactViewer artifacts={artifacts} />
          </div>
        </div>
      </main>
    </div>
  );
}
