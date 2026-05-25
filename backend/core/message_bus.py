import asyncio
import uuid
from typing import Dict, List, Callable, Any
from datetime import datetime

class Message:
    def __init__(self, sender: str, receiver: str, content: str, msg_type: str, metadata: Dict = None):
        self.id = str(uuid.uuid4())
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.msg_type = msg_type  # task, result, feedback, status
        self.metadata = metadata or {}
        self.timestamp = datetime.now().isoformat()
        self.status = "pending"

    def to_dict(self):
        return {
            "id": self.id,
            "sender": self.sender,
            "receiver": self.receiver,
            "content": self.content,
            "msg_type": self.msg_type,
            "metadata": self.metadata,
            "timestamp": self.timestamp,
            "status": self.status
        }

class MessageBus:
    """Central communication hub for all agents."""
    
    def __init__(self):
        self.subscribers: Dict[str, List[Callable]] = {}
        self.message_history: List[Dict] = []
        self.broadcast_callbacks: List[Callable] = []
    
    def subscribe(self, agent_name: str, callback: Callable):
        if agent_name not in self.subscribers:
            self.subscribers[agent_name] = []
        self.subscribers[agent_name].append(callback)
    
    def subscribe_broadcast(self, callback: Callable):
        self.broadcast_callbacks.append(callback)
    
    async def publish(self, message: Message):
        self.message_history.append(message.to_dict())
        
        for callback in self.broadcast_callbacks:
            await callback(message.to_dict())
            
        if message.receiver in self.subscribers:
            for callback in self.subscribers[message.receiver]:
                await callback(message)
    
    def get_history(self):
        return self.message_history
