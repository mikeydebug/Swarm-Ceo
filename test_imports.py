import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "backend"))
from agents.orchestrator import SwarmOrchestrator
print("Orchestrator imported successfully!")
