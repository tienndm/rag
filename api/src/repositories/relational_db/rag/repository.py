"""Relational database repository implementation."""

from typing import Callable, List, Optional, Dict, Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.sql import delete, func, insert, select, update

from common.types import UUIDStr
from models.exception import RagNotFound
from models.rag import *

from ...abstraction.rag import AbstractRagRepository
from .mapper import ConversationsMapper, ChatsMapper
from .orm import *

func: Callable


class RelationalDBRagRepository(AbstractRagRepository):
    """SQL implementation of RagRepository."""

    async def getConversation(
        self, userId: UUIDStr, params: Optional[GetConversationsParamsModel] = None
    ) -> List[ConversationsModel]:
        stmt = (
            select(Conversation)
            .where(Conversation.user_id == userId)
            .options(
                selectinload(Conversation.name),
                selectinload(Conversation.user_id),
                selectinload(Conversation.messages),
            )
        )
        if params:
            stmt = stmt.offset((params.page - 1) * params.size).limit(params.size)
        result = await self.session.execute(stmt)
        conversations = result.scalars().all()
        if not conversations:
            raise RagNotFound
        return list(map(ConversationsMapper.ormToEntity, conversations))

    async def getChats(
        self, conversationId: UUIDStr, params: Optional[GetChatsParamsModel] = None
    ) -> List[ChatsModel]:
        stmt = (
            select(ChatMessage)
            .where(ChatMessage.conversation_id == conversationId)
            .order_by(ChatMessage.created_at.desc())
        )
        if params:
            stmt = stmt.offset((params.page - 1) * params.size).limit(params.size)
        result = await self.session.execute(stmt)
        chats = result.scalars().all()
        if not chats:
            raise RagNotFound
        return list(map(ChatsMapper.ormToEntity, chats))

    async def createChat(self, data: CreateChatsModel) -> int:
        stmt = (
            insert(ChatMessage)
            .values(
                chat_role_id=data.chatRoleId,
                conversation_id=data.conversationId,
                message=data.message,
            )
            .returning(ChatMessage.id)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one()
    
    async def createConversation(self, data: CreateConversationModel) -> UUIDStr:
        stmt = (
            insert(Conversation)
            .values(
                name=data.name,
                user_id=data.userId
            )
            .returning(Conversation.id)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one()

    async def delete(self, data: DeleteModel):
        stmt = delete(Conversation).where(Conversation.id == data.conversationId)
        result = await self.session.execute(stmt)
        if result.rowcount == 0:
            raise RagNotFound

