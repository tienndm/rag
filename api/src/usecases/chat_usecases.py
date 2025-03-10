from typing import Any, Tuple
from common.utils import build_uuid4_str
from common.types import UUIDStr

from di.unit_of_work import AbstractUnitOfWork
from models.rag import *


async def getConversations(
    asyncUnitOfWork: AbstractUnitOfWork,
    userId: UUIDStr,
    params: Optional[GetConversationsParamsModel] = None,
) -> list[ConversationsModel]:
    async with asyncUnitOfWork as auow:
        return await auow.ragRepo.getConversation(userId=userId, params=params)


async def getChats(
    asyncUnitOfWork: AbstractUnitOfWork,
    conversationId: UUIDStr,
    params: Optional[GetChatsParamsModel] = None,
) -> list[ChatsModel]:
    async with asyncUnitOfWork as auow:
        return await auow.ragRepo.getChats(conversationId=conversationId, params=params)


async def createChat(
    asyncUnitOfWork: AbstractUnitOfWork, input: CreateChatsModel
) -> str:
    async with asyncUnitOfWork as auow:
        await auow.ragRepo.createChat(data=input)
    # TODO Generate answer
    response = "Xin chào"
    async with asyncUnitOfWork as auow:
        data = CreateChatsModel(
            chatRoleId=2, conversationId=input.conversationId, message=response
        )
        await auow.ragRepo.createChat(data)
    return response
