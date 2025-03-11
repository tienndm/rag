"""Rag domain models."""

from dataclasses import dataclass, field
from typing import Optional

from common.types import UUIDStr


@dataclass
class GetChatsParamsModel:
    page: int = 1
    size: int = 10


@dataclass
class GetConversationsParamsModel:
    page: int = 1
    size: int = 10


@dataclass
class ConversationsModel:
    id: UUIDStr
    name: str
    userId: UUIDStr


@dataclass
class ChatsModel:
    id: int
    chatRoleId: int
    conversationId: UUIDStr
    message: str


@dataclass
class ChatRoles:
    id: int
    role: str


@dataclass
class CreateConversationModel:
    id: str
    name: str
    userId: UUIDStr


@dataclass
class UpdateConversationModel:
    id: str
    name: str


@dataclass
class CreateChatsModel:
    conversationId: UUIDStr
    message: str
    chatRoleId: int


@dataclass
class DeleteModel:
    conversationId: UUIDStr
