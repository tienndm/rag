"""Abstract repository interfaces for rag."""

from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession


from common.types import UUIDStr
from models.rag import *


class AbstractRagRepository(ABC):
    """Abstract repository for rag."""
    session: any
    def __init__(self, session: AsyncSession):
        self.session = session

    @abstractmethod
    def getConversation(
        self, userId: UUIDStr, params: Optional[GetConversationsParamsModel]
    ) -> list[ConversationsModel]:
        raise NotImplementedError

    @abstractmethod
    def getChats(
        self, conversationId: UUIDStr, params: Optional[GetChatsParamsModel]
    ) -> list[ChatsModel]:
        raise NotImplementedError

    @abstractmethod
    def createChat(self, data: CreateChatsModel) -> int:
        raise NotImplementedError

    @abstractmethod
    def createConversation(self, data: CreateConversationModel) -> UUIDStr:
        raise NotImplementedError
    
    @abstractmethod
    def updateConversation(self, data: UpdateConversationModel):
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: UUIDStr):
        raise NotImplementedError