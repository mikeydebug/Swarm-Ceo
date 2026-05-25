import React from 'react';
import { motion } from 'framer-motion';
import { Code2 } from 'lucide-react';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism';
import './ArtifactViewer.css';

export default function ArtifactViewer({ artifacts }) {
  const fileNames = Object.keys(artifacts || {});
  const [activeFile, setActiveFile] = React.useState(fileNames[0]);

  React.useEffect(() => {
    if (fileNames.length > 0 && !activeFile) {
      setActiveFile(fileNames[0]);
    }
  }, [fileNames, activeFile]);

  // Determine language for syntax highlighting based on extension
  const getLanguage = (filename) => {
    if (!filename) return 'javascript';
    if (filename.endsWith('.py')) return 'python';
    if (filename.endsWith('.js') || filename.endsWith('.jsx')) return 'javascript';
    if (filename.endsWith('.html')) return 'html';
    if (filename.endsWith('.css')) return 'css';
    if (filename.endsWith('.json')) return 'json';
    if (filename.endsWith('.md')) return 'markdown';
    return 'javascript';
  };

  return (
    <div className="artifacts-container glass-panel">
      <div className="panel-header">
        <h2><Code2 size={18} /> Generated Artifacts</h2>
      </div>
      <div className="artifacts-content">
        {fileNames.length === 0 ? (
          <div className="artifacts-empty">No artifacts generated yet.</div>
        ) : (
          <div className="artifacts-split">
            <div className="file-list">
              {fileNames.map(f => (
                <div 
                  key={f} 
                  className={`file-item ${activeFile === f ? 'active' : ''}`}
                  onClick={() => setActiveFile(f)}
                >
                  {f}
                </div>
              ))}
            </div>
            <div className="code-viewer">
              <SyntaxHighlighter 
                language={getLanguage(activeFile)} 
                style={vscDarkPlus}
                customStyle={{ margin: 0, padding: '1rem', background: 'transparent', fontSize: '14px', height: '100%' }}
                wrapLines={true}
                wrapLongLines={true}
              >
                {artifacts[activeFile]}
              </SyntaxHighlighter>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
