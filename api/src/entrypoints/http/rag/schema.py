"""HTTP request/response schema definitions."""
from typing import Optional

from pydantic import BaseModel

from common.types import UUIDStr, DateTime

class ChatRequest(BaseModel):
    userId: str
    conversationId: str
    message: str

class ChatResponse(BaseModel):
    id: int
    chatRole: int
    conversationId: str
    messages: str

class ConversationResponse(BaseModel):
    id: str
    name: str
    userId: str