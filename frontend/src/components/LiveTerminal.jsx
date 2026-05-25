import React from 'react';
import { Terminal } from 'lucide-react';
import './LiveTerminal.css';

export default function LiveTerminal({ logs }) {
  return (
    <div className="terminal-container glass-panel">
      <div className="panel-header">
        <h2><Terminal size={18} /> Execution Terminal</h2>
      </div>
      <div className="terminal-content panel-content">
        {logs.length === 0 ? (
          <div className="terminal-empty">Awaiting instructions...</div>
        ) : (
          logs.map((log, i) => (
            <div key={i} className={`log-entry ${log.type}`}>
              <span className="log-time">[{new Date(log.timestamp).toLocaleTimeString()}]</span>
              <span className="log-message">{log.data.message}</span>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
