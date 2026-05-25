import React from 'react';
import { motion } from 'framer-motion';
import { BrainCircuit } from 'lucide-react';
import './SwarmVisualizer.css';

const AGENTS = [
  { id: 'ManagerAgent', label: 'Manager', icon: '👨‍💼', phase: 'Management' },
  { id: 'ResearchAgent', label: 'Researcher', icon: '🌐', phase: 'Research' },
  { id: 'PlannerAgent', label: 'Planner', icon: '🧠', phase: 'Planning' },
  { id: 'CoderAgent', label: 'Coder', icon: '💻', phase: 'Coding' },
  { id: 'SecurityAgent', label: 'Security', icon: '🛡️', phase: 'Security' },
  { id: 'ReviewerAgent', label: 'Reviewer', icon: '🔍', phase: 'Review' },
];

export default function SwarmVisualizer({ currentPhase, agentStatuses }) {
  return (
    <div className="visualizer-wrapper">
      {/* Left Side: CEO */}
      <div className="ceo-section">
        <motion.div 
          animate={{ scale: currentPhase && currentPhase !== 'Complete' ? [1, 1.05, 1] : 1 }}
          transition={{ repeat: Infinity, duration: 2 }}
          className="ceo-node"
        >
          <div className="ceo-glow"></div>
          <BrainCircuit size={48} className="ceo-icon" />
          <div className="ceo-label">Swarm CEO</div>
        </motion.div>
      </div>

      {/* Connection Lines (Visual only) */}
      <div className="connection-divider">
        {currentPhase && currentPhase !== 'Complete' && (
          <motion.div 
            className="active-data-stream"
            initial={{ height: '0%' }}
            animate={{ height: '100%' }}
            transition={{ repeat: Infinity, duration: 1.5 }}
          />
        )}
      </div>

      {/* Right Side: Agents Grid */}
      <div className="agents-grid">
        {AGENTS.map((agent) => {
          const isActive = currentPhase === agent.phase;
          const status = agentStatuses[agent.id];
          
          return (
            <motion.div 
              key={agent.id}
              className={`agent-card glass-panel ${isActive ? 'active' : ''}`}
              animate={isActive ? { y: -5 } : { y: 0 }}
              transition={{ duration: 0.3 }}
            >
              <div className="agent-icon-wrapper">
                <span className="agent-icon">{agent.icon}</span>
                {isActive && (
                  <motion.div 
                    className="active-ring"
                    animate={{ rotate: 360 }}
                    transition={{ repeat: Infinity, duration: 3, ease: "linear" }}
                  />
                )}
              </div>
              <div className="agent-info">
                <h3>{agent.label}</h3>
                <div className={`agent-status ${isActive ? 'pulsing' : ''}`}>
                  {status || 'Idle'}
                </div>
              </div>
            </motion.div>
          );
        })}
      </div>
    </div>
  );
}
